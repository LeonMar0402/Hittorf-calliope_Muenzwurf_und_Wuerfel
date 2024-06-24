input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Würfel_oder_Münzwurf = 1
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Würfel_oder_Münzwurf = 2
})
let Würfel_oder_Münzwurf = 0
let einmal = 0
let Kopf_oder_Zahl = 0
Würfel_oder_Münzwurf = 0
basic.showString("Würfel- oder Münzwurf? [a/b]")
basic.forever(function () {
    if (Würfel_oder_Münzwurf == 1) {
        if (einmal == 0) {
            basic.showString("Schütel um den Würfel zu werfen.")
            einmal = 1
        }
        if (input.isGesture(Gesture.Shake)) {
            basic.showString("" + (randint(1, 6)))
        }
    }
    if (Würfel_oder_Münzwurf == 2) {
        if (einmal == 0) {
            basic.showString("Schütel um die Münze zu werfen.", 200)
            einmal = 1
        }
        if (input.isGesture(Gesture.Shake)) {
            Kopf_oder_Zahl = randint(1, 2)
            if (Kopf_oder_Zahl == 1) {
                basic.showString("Kopf")
            }
            if (Kopf_oder_Zahl == 2) {
                basic.showString("Zahl")
            }
        }
    }
})
