# HEMAScorer 

This application is designed to be able to be used to record scores and compute bout pairings for HEMA competitons.

# Spec

* User-friendly, intuitive UI
  * Clear display of combatant names (and corner colours)
    * Fighters on deck
  * Clear display of scores for the two combatants
  * Input controls to modify scores
    * Add/subtract points
    * Doubles
    * Warnings
    * Dismissal of last entered score
      * Authentication to prevent tampering?
    * Automatically end bout when score cap reached
  * Timer
    * Starting and stopping in line with referee consultation
    * Warning when time limit about to be exceeded
      * 3 min max run time
        * Automatically finish bout when time exceeded
      * 10 second warning prior to time expiration for last exchange
  * Support for calculation of bout pairings
    * Round-robin pool
    * Swiss system
    * Others?
    * Display past and upcoming bouts
      * Highlight current bout
  * Support for multi-round matchups
    * Pool stage, elimination stage, etc
  * Support for input from multiple pools performed on other machines
    * Network capability for inter-machine communication?
    * Internet connection not required, P2P should more than suffice
  * Authentication? Prevent foul play
