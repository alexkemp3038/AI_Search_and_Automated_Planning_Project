(define (problem lunar-mission-3)
    (:domain lunar-extended)

    (:objects
        alice bob - astronaut
        lander1 lander2 - lander
        rover1 rover2 - rover
        wp1 wp2 wp3 wp4 wp5 wp6 - waypoint
        sample5 sample1 - sample
        image3 image2 - image
        scan4 scan6 - scan  
        cr1 cr2 - controlRoom
        db1 db2 - dockingBay  
    )

    ; -------------------------------
    ; Initial State
    ; -------------------------------

    (:init
        ; --- Lander 1 ---
        (landed-at lander1 wp2) ; lander1 begins as landed at wp2
        (lander-sample-free lander1) ; sample slot free

         ; --- Rover 1 ---
        (rover-lander rover1 lander1) ; ownership (static)
        (rover-at rover1 wp2) ; begins deployed at wp2
        (rover-data-free rover1) ; data slot free
        (rover-sample-free rover1) ; sample slot free

        ; --- Lander 2 ---
        (in-orbit lander2) ; not landed yet
        (lander-sample-free lander2) ; sample slot free

        ; --- Rover 2 ---
        (rover-lander rover2 lander2) ; ownership (static)
        (rover-onboard rover2) ; begins undeployed
        (rover-data-free rover2) ; data slot free
        (rover-sample-free rover2) ; sample slot free

        ; --- Connectivity ---
        (connected wp1 wp2) ; wp1 -> wp2
        (connected wp2 wp1) ; wp2 -> wp1
        (connected wp2 wp4) ; wp2 -> wp4
        (connected wp4 wp2) ; wp4 -> wp2
        (connected wp2 wp3) ; wp2 -> wp3
        (connected wp6 wp4) ; wp6 -> wp4
        (connected wp5 wp6) ; wp5 -> wp6
        (connected wp5 wp3) ; wp5 -> wp3
        (connected wp3 wp5) ; wp3 -> wp5

        ; --- Images and Scans ---
        (data-at image3 wp3)
        (data-at image2 wp2)
        (data-at scan4 wp4)
        (data-at scan6 wp6)

        ; --- Ground Samples ---
        (sample-at sample5 wp5)
        (sample-at sample1 wp1)

        ; --- Connect Rooms ---
        (lander-rooms lander1 cr1)
        (lander-rooms lander1 db1)
        (lander-rooms lander2 cr2)
        (lander-rooms lander2 db2)

        ; --- Control Room's and Docking Bay's ---
        (connect-rooms cr1 db1)
        (connect-rooms db1 cr1)
        (connect-rooms cr2 db2)
        (connect-rooms db2 cr2)

        ; --- Astronauts ---
        (astronaut-lander alice lander1) ; alice belongs to lander 1
        (astronaut-lander bob lander2) ; bob belongs to lander 2
        (astronaut-at alice db1) ; alice is in lander 1's docking bay
        (astronaut-at bob cr2) ; bob is in lander 2's control room
    )

    (:goal
        (and
            (transmitted-data lander1 image3)
            (transmitted-data lander2 scan4)
            (transmitted-data lander2 image2)
            (transmitted-data lander1 scan6)
            (lander-sample lander1 sample5)
            (lander-sample lander2 sample1)
        )
    )
)