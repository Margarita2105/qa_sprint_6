from datetime import datetime, timedelta

class Data:
    how_much = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    several_scooters = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    rental_time = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    scooter_today = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    extend_or_return = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    charger = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    cancel = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    mkad = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    list_question = [how_much, several_scooters, rental_time, scooter_today, extend_or_return, charger, cancel, mkad]
    name_1 = 'Мария'
    name_2 = 'Иван'
    sname_1 = 'Иванова'
    sname_2 = 'Петров'
    adress_1 = 'Усачева'
    adress_2 = 'Усачева,1'
    metro_1 = 'Сокольники'
    metro_2 = 'Черкизовская'
    telephone_1 = '+79554342278'
    telephone_2 = '+79111111111'
    renta_1 = 'сутки'
    renta_2 = 'двое суток'
    comment_1 = 'Привезите'
    comment_2 = 'Привезите мне'
    win_text = 'Хотите оформить заказ?'

class Time:
    currentTimeDate_1 = datetime.now() + timedelta(days=1)
    currentTimeDate_2 = datetime.now() + timedelta(days=2)
    if currentTimeDate_1.strftime('%d').startswith('0'):
        currentTime_1 = currentTimeDate_1.strftime('%d').replace("0", "", 1)
    else:
        currentTime_1 = currentTimeDate_1.strftime('%d')
    if currentTimeDate_2.strftime('%d').startswith('0'):
        currentTime_2 = currentTimeDate_2.strftime('%d').replace("0", "", 1)
    else:
        currentTime_2 = currentTimeDate_2.strftime('%d')
