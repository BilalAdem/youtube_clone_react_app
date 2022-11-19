from Booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2022-07-19',
                         check_out_date='2022-07-25')
        bot.select_adults(1)
        bot.click_search()
        bot.refresh()
        print(""" __________               __   .__                      
\______   \ ____   ____ |  | _|__| ____    ____        
 |    |  _//  _ \ /  _ \|  |/ /  |/    \  / ___\       
 |    |   (  <_> |  <_> )    <|  |   |  \/ /_/  >      
 |______  /\____/ \____/|__|_ \__|___|  /\___  /       
        \/                   \/       \//_____/        
  ___ ___                __     __________        __   
 /   |   \_____    ____ |  | __ \______   \ _____/  |_ 
/    ~    \__  \ _/ ___\|  |/ /  |    |  _//  _ \   __\
\    Y    // __ \\  \___|    <   |    |   (  <_> )  |  
 \___|_  /(____  /\___  >__|_ \  |______  /\____/|__|  
       \/      \/     \/     \/         \/             
       
       
        the bot will start... """)
        bot.report_result()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
