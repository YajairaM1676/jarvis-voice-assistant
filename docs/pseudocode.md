START PROGRAM

IMPORT speech recognition module
IMPORT wikipedia_oop module

CREATE Jarvis program loop

WHILE program is running
    GET user voice command using get_command()

    IF command contains "wikipedia"
        ASK user what they want to search
        CALL get_wikipedia(search_term)
        DISPLAY result

    ELSE IF command contains "exit" OR "quit"
        DISPLAY goodbye message
        STOP program

    ELSE
        DISPLAY "Command not recognized"

END WHILE

END PROGRAM
