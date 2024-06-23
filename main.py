def on_button_a():
    global Würfel_oder_Münzwurf
    basic.show_string("hi!")
    Würfel_oder_Münzwurf = 1
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    global Würfel_oder_Münzwurf
    Würfel_oder_Münzwurf = 2
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

Würfel_oder_Münzwurf = 0
Kopf_oder_Zahl = 0
Würfel_oder_Münzwurf = 0
basic.show_string("Würfel- oder Münzwurf? [a/b]")

def on_forever():
    global Kopf_oder_Zahl
    if Würfel_oder_Münzwurf == 1:
        basic.show_string("Schütel um den Würfel zu werfen.")
        if input.is_gesture(Gesture.SHAKE):
            basic.show_string("" + str((randint(1, 6))))
    if Würfel_oder_Münzwurf == 2:
        basic.show_string("Schütel um die Münze zu werfen.")
        if input.is_gesture(Gesture.SHAKE):
            Kopf_oder_Zahl = randint(1, 2)
            if Kopf_oder_Zahl == 1:
                basic.show_string("Kopf")
            if Kopf_oder_Zahl == 2:
                basic.show_string("Zahl")
basic.forever(on_forever)
