# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Разум', color="#c8ffc8")
define ya = Character('Я', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    $ bg_music = "music/bg.mp3"



# Игра начинается здесь:
label start:
    play music bg_music
    
    scene bg room
    
    pause 3

    show mind

    e "Ты ещё не сделал ничего стоящего в этой жизни."

    e "Даже ни одной игры.."

    e "Ни одной новеллы.."

    ya "..."

    e "Подумай об этом, и скажи мне.."

    menu:
        "Я бросаю работу и начинаю делать игру!":
            e "Так держать!"
            pause 1
            jump s1

        "Пожалуй меня всё устраивает.":
            ya "Спасибо за предложение"
            pause 1
            jump s2

        "Го в доту! Я создал!":
            e "Не плохо!"
            pause 1
            jump s3



    return

label s1:
    scene bg_s1
    
    e "И не забывай про того..."
    
    e "Кто тебя подтолкнул к этому ;)"
    
    pause 3
    
    return

label s2:
    scene bg_s2
    
    ya "Но меня устраивает моя жизнь."
    
    e "Слабак..."
    
    pause 3
    
    return
    
label s3:
    scene bg_s3

    e "Но..."

    e "Мид или фид!"

    pause 3

    return