(define (problem lunar-mission-1)
    (:domain lunar)

    (:objects
        lander1 - lander
        rover1 - rover
        wp1 wp2 wp3 wp4 wp5 - waypoint
        sample1 - sample
        image5 - image
        scan3 - scan
    )

    ; -------------------------------
    ; Initial State
    ; -------------------------------

    (:init
        ; --- Lander ---
        (in-orbit lander1) ; not landed yet
        (lander-sample-free lander1) ; sample slot free

        ; --- Rovers ---
        (rover-lander rover1 lander1) ; ownership (static)
        (rover-onboard rover1) ; begins undeployed
        (rover-data-free rover1) ; data slot free
        (rover-sample-free rover1) ; sample slot free

        ; --- Connectivity ---
        (connected wp1 wp2) ; wp1 -> wp2
        (connected wp2 wp3) ; wp2 -> wp3
        (connected wp1 wp4) ; wp1 -> wp4
        (connected wp4 wp3) ; wp4 -> wp3
        (connected wp3 wp5) ; wp3 -> wp5
        (connected wp5 wp1) ; wp5 -> wp1

        ; --- Images and Scans ---
        (data-at image5 wp5)
        (data-at scan3 wp3)

        ; --- Ground Samples ---
        (sample-at sample1 wp1)
    )

    (:goal
        (and
            (transmitted-data lander1 image5)
            (transmitted-data lander1 scan3)
            (lander-sample lander1 sample1)
        )
    )
)