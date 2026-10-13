(define (domain lunar-extended)
    (:requirements :strips :typing)

    ; -------------------------------
    ; Types
    ; -------------------------------

    (:types
    astronaut lander rover waypoint sample data rooms - object
    image scan - data
    controlRoom dockingBay - rooms
    )
    ; -------------------------------
    ; Predicates
    ; -------------------------------

    (:predicates
        ; Which lander an astronaut belongs to.
        (astronaut-lander ?a - astronaut ?l - lander)

        ; Tracks current room of an astronaut.
        (astronaut-at ?a - astronaut ?ro - rooms)

        ; Links a lander to its internal rooms.
        (lander-rooms ?l - lander ?ro - rooms)

        ; Connects a control room to its docking bay.
        (connect-rooms ?cr - controlRoom ?db - dockingBay)

        ; Keeps record of rovers corresponding lander.
        (rover-lander ?r - rover ?l - lander)

        ; Checks if lander is still in orbit
        (in-orbit ?l - lander)

        ; Gives waypoint of where lander landed
        (landed-at ?l - lander ?w - waypoint)

        ; Checks if rover is onboard.
        (rover-onboard ?r - rover)

        ; Location of rover
        (rover-at ?r - rover ?w - waypoint)

        ; Location of ground sample
        (sample-at ?s - sample ?w - waypoint)

        ; Checks connectivity of two waypoints
        (connected ?from ?to - waypoint)

        ; Waypoint where data ?d is captured.
        (data-at ?d - data ?w - waypoint)

        ; Records the image a rover is carrying
        (rover-data ?r - rover ?d - data) 

        ; Data that has been transmitted to this lander
        (transmitted-data ?l - lander ?d - data)

        ; Checks if rover is carrying item of data
        (rover-data-free ?r - rover)

        ; Records the sample a rover is carrying
        (rover-sample ?r - rover ?s - sample) 

        ; Checks if rover is carrying any samples
        (rover-sample-free ?r - rover)

        ; Records sample lander is storing
        (lander-sample ?l - lander ?s - sample)

        ; Checks if lander is storing any sample
        (lander-sample-free ?l - lander)
    )

    ; -------------------------------
    ; Actions
    ; -------------------------------
    
    (:action move_astronaut
        :parameters (?a - astronaut ?l - lander ?from - rooms ?to - rooms)

        ; To move an astronaut:
        ; 1. The astronaut must be in the lander
        ; 2. The astronaut must be in the 'from' room
        ; 3. The 'from' room must be connected to the 'to' room.
        ; 4. The 'from' and 'to' rooms must be connected to the lander.
        :precondition (and (astronaut-lander ?a ?l)
                           (astronaut-at ?a ?from)
                           (lander-rooms ?l ?from)
                           (lander-rooms ?l ?to)
                           (connect-rooms ?from ?to))

        ; Now the astronaut is in the 'to' room and not in the 'from' room.
        :effect (and (not (astronaut-at ?a ?from) )
                     (astronaut-at ?a ?to))
    )   

    (:action land_lander
        :parameters (?l - lander ?w - waypoint)

        ; To land lander it must be in orbit.
        :precondition (and (in-orbit ?l) )

        ; Now the landed has landed at the waypoint and its not in orbit.
        :effect (and (landed-at ?l ?w)
                     (not (in-orbit ?l) ))
    )

    (:action move_rover
        :parameters (?r - rover ?from - waypoint ?to - waypoint)
    
        ; To move the rover:
        ; 1. The rover must be at waypoint 'from'
        ; 2. Waypoint 'from' must be connected to 'to' in that direction.
        :precondition (and (rover-at ?r ?from)
                            (connected ?from ?to))
    
        ; Now, rover is at waypoint 'to', and not at 'from'
        :effect (and (not (rover-at ?r ?from) )
                     (rover-at ?r ?to))
    )   


    (:action deploy_rover
        :parameters (?r - rover ?l - lander ?w - waypoint ?a - astronaut ?db - dockingBay)

        ; To deploy rover, it:
        ; 1. Must be onboard (not yet deployed).
        ; 2. Must be on corresponding lander.
        ; 3. The lander must have landed.
        ; 4. An astronaut must be in the lander.
        ; 5. An astronaut must be in that landers docking bay.

        :precondition (and (rover-onboard ?r)
                           (rover-lander ?r ?l)
                           (landed-at ?l ?w)
                           (astronaut-lander ?a ?l)
                           (astronaut-at ?a ?db)
                           (lander-rooms ?l ?db))

        ; Now the rover is deployed at the given waypoint
        ; and it indicates its no longer onboard.
        :effect (and (rover-at ?r ?w)
                     (not (rover-onboard ?r) ))
    )

    (:action rover_acquire_data
        :parameters (?r - rover ?w - waypoint ?d - data)

        ; For a rover to acquire image:
        ; 1. The rover must currently not carry any items of data.
        ; 2. (Assumption) The rover must be deployed
        ; 3. The rover must be at the waypoint where the data is captured.
        :precondition (and (rover-data-free ?r)
                           (rover-at ?r ?w)
                           (data-at ?d ?w))
    
        ; Now rovers data slot is no longer free and is carrying data.
        :effect (and (not (rover-data-free ?r) )
                (rover-data ?r ?d))
    )

    (:action rover_transmit_data
        :parameters (?r - rover ?l - lander ?d - data ?a - astronaut ?cr - controlRoom)

        ; For a rover to transmit an image:
        ; 1. It must be carrying an item of data
        ; 2. The rover must belong to that lander
        ; 3. An astronaut must be in the lander.
        ; 4. An astronaut must be in that landers control room.
        :precondition (and (rover-lander ?r ?l)
                           (rover-data ?r ?d)
                           (astronaut-lander ?a ?l)
                           (astronaut-at ?a ?cr)
                           (lander-rooms ?l ?cr))

        ; Lander has received the data and rovers memory is free'd.
        :effect (and (not (rover-data ?r ?d) )
                     (rover-data-free ?r)
                     (transmitted-data ?l ?d))
    )

    (:action rover_collect_sample
        :parameters (?r - rover ?w - waypoint ?s - sample)

        ; For a rover to collect a sample:
        ; 1. The rover must not be holding any other samples.
        ; 2. The rover must be at the samples waypoint
        :precondition (and (rover-sample-free ?r)
                           (sample-at ?s ?w)
                           (rover-at ?r ?w))

        ; Now the rover is carrying the sample and the sample is
        ; no longer on the ground.
        :effect (and (rover-sample ?r ?s)
                     (not (rover-sample-free ?r) )
                     (not (sample-at ?s ?w) ))
    )

    (:action rover_store_sample
        :parameters (?r - rover ?l - lander ?w - waypoint ?s - sample ?a - astronaut ?db - dockingBay)

        ; For a rover to store a sample:
        ; 1. The rover must be holding the corresponding sample.
        ; 2. The rover must be at the landers waypoint.
        ; 3. The lander thats storing the sample should be that rovers lander.
        ; 4. The landers sample slot must be empty.
        ; 5. An astronaut must be in the lander.
        ; 6. An astronaut must be in that landers docking bay.
        :precondition (and (rover-sample ?r ?s)
                           (rover-at ?r ?w)
                           (landed-at ?l ?w)
                           (rover-lander ?r ?l)
                           (lander-sample-free ?l)
                           (astronaut-lander ?a ?l)
                           (astronaut-at ?a ?db)
                           (lander-rooms ?l ?db)) 

        ; Now:
        ; 1. The sample is stored in the lander
        ; 2. The rovers collect slot is free'd
        :effect (and (lander-sample ?l ?s)
                     (not (rover-sample ?r ?s) )
                     (rover-sample-free ?r)
                     (not (lander-sample-free ?l) ))
    )
)