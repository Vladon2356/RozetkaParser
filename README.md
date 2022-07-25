Task 1 

Rozetka parser with Selenium 

Script have dict with filter params, sort_by and count_to_compare params.

Scripts steps :

1. Open Chrome window
2. Get link - https://rozetka.com.ua/ua/
3. Click on category - 'Смартфони, ТВ і Електроніка'
4. On new page click on - 'Мобільні телефони'
5. Add filters from filter_params dict
6. Sort result by sort_by param
7. Add to compare count_to_compare products
8. Redirect to compare page
9. Click on new page on 'Тільки відмінності'
10. End work

# Setup

1. Clone the repository
    ```sh
   git clone https://github.com/Vladon2356/RozetkaParser.git
   cd RozetkaParser
   ```
2. Create virtual environments
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Run script 
   ```sh
   python main.py
   ```
