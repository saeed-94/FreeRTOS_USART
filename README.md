<!-- Add this at the top of your README file -->



<details id="english">
  <summary>English</summary>

  <lang dir="ltr">


# Arduino-PyQt Interface

This project combines an Arduino simulation and a PyQt graphical user interface to interact with the simulated Arduino device. Below, you'll find comprehensive explanations for both the Arduino and PyQt components.

## Arduino Code

The Arduino code (`projects.ino`) generates and transmits simulated data to mimic the behavior of a real Arduino device. Here is a detailed explanation of the Arduino code:

### Arduino Code Logic

- **Semaphore:** The Arduino code utilizes a semaphore (`xSerialSemaphore`) to synchronize access to Serial communication.

- **TaskSerialSend Function:**
  - Generates a random 3-digit variable value (`variableData`).
  - Generates a random 3-bit low value (`lowBits`).
  - Constructs a data string in the format: `AABBCCIDXXX\n`.
  - Sends the data through the Serial port using a mutex to avoid conflicts.

### Setup Function

- Initializes Serial communication.
- Creates a semaphore (`xSerialSemaphore`).
- Creates a FreeRTOS task (`taskSerialSend`) to handle the continuous generation and transmission of data.

### Loop Function

- The `loop` function remains empty as most of the logic is implemented in FreeRTOS tasks.

## PyQt Graphical User Interface

The PyQt code (`gui.py`) serves as the graphical user interface (GUI) for interacting with the simulated Arduino device. Below is a comprehensive overview of the PyQt code:

### Styling

- **Dark Mode Palette:** The application adopts an aesthetically pleasing dark mode palette for a modern and visually appealing user interface.
- **Font:** The chosen font is "Segoe UI" with a size of 14, contributing to a clean and contemporary design.

### User Interface Elements

- **Data Display Section:** QLabel and QTextEdit elements are intelligently arranged to provide a user-friendly display for received data. The QTextEdit widget is set to read-only mode to prevent user input.
- **Control Buttons:** Two buttons, "Refresh Serial Ports" and "Connect," offer seamless interaction for the user.

### Functionality

- **Refresh Serial Ports:** Upon clicking the "Refresh Serial Ports" button, the application queries and displays the available serial ports using the `serial.tools.list_ports` module.
- **Connect to Arduino:** Clicking the "Connect" button establishes a connection to the specified Arduino port and initiates the `SerialThread` for continuous data reception.

### SerialThread Class

- **Threaded Operation:** Utilizes PyQt's QThread to perform tasks concurrently with the main application thread.
- **Data Reception:** Monitors the serial port for incoming data and emits a pyqtSignal (`data_received`) when data is received.
- **Stop Thread:** Implements a method (`stop_thread`) to gracefully stop the thread.

## Running the Application

To execute the application, follow the instructions provided in the "Usage" section of this README.

## Schematic Diagram

![Schematic Diagram](/Shematic.png)

## Project Demonstration Video

[Watch Project Demonstration](/Video.mkv)
## Video Demonstration
<video width="٪100" height="100" controls>
  <source src="/Video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

[![Watch the video](/Shematic.png)](/Video.mp4)


## Acknowledgments

Heartfelt thanks to all contributors who have played a role in improving and enhancing this project.


...
  </lang>
</details>

<details id="فارسی">
  <summary>فارسی</summary>



<lang dir="rtl">
# رابط Arduino-PyQt

این پروژه یک شبیه‌سازی Arduino و یک رابط کاربری گرافیکی PyQt را ترکیب می‌کند تا با دستگاه Arduino شبیه‌سازی شده تعامل داشته باشد. در زیر، توضیحات جامعی برای هر دو بخش Arduino و PyQt آورده شده است.

## کد Arduino

کد Arduino (`projects.ino`) داده‌های شبیه‌سازی شده را ایجاد و ارسال می‌کند تا رفتار یک دستگاه واقعی Arduino را تقلید کند. در ادامه توضیح دقیقی از کد Arduino آورده شده است:

### منطق کد Arduino

- **سمافور:** کد Arduino از یک سمافور (`xSerialSemaphore`) برای همگام‌سازی دسترسی به ارتباط Serial استفاده می‌کند.

- **تابع TaskSerialSend:**
  - یک مقدار تصادفی 3 رقمی برای متغیر ایجاد می‌کند (`variableData`).
  - یک مقدار تصادفی 3 بیتی برای مقدار پایین ایجاد می‌کند (`lowBits`).
  - یک رشته داده به فرمت `AABBCCIDXXX\n` ایجاد می‌کند.
  - داده را از طریق پورت Serial ارسال می‌کند با استفاده از یک mutex برای جلوگیری از تداخل‌ها.

### تابع Setup

- ارتباط Serial را مقداردهی اولیه می‌کند.
- یک سمافور ایجاد می‌کند (`xSerialSemaphore`).
- یک وظیفه FreeRTOS (`taskSerialSend`) برای مدیریت تولید و انتقال مداوم داده ایجاد می‌کند.

### تابع Loop

- تابع `loop` خالی می‌ماند زیرا بیشتر منطق در وظایف FreeRTOS اجرا شده است.

## رابط گرافیکی PyQt

کد PyQt (`gui.py`) به عنوان رابط کاربری گرافیکی (GUI) برای تعامل با دستگاه Arduino شبیه‌سازی شده عمل می‌کند. در زیر، یک مرور جامع از کد PyQt آورده شده است:

### استایل

- **پالت حالت تاریک:** برنامه از یک پالت حالت تاریک زیبا برای یک رابط کاربری نوین و جذاب استفاده می‌کند.
- **فونت:** فونت انتخابی "Segoe UI" با اندازه 14 است که به طراحی تمیز و معاصر کمک می‌کند.

### عناصر رابط کاربری

- **بخش نمایش داده‌ها:** عناصر QLabel و QTextEdit به طریق هوشمندانه برای ارائه یک نمایش کاربر پسند از داده‌های دریافتی استفاده شده‌اند. ویجت QTextEdit به حالت فقط خواندن تنظیم شده است تا ورودی کاربر را جلوگیری کند.
- **دکمه‌های کنترل:** دو دکمه "Refresh Serial Ports" و "Connect" امکان تعامل بی‌دردسر با کاربر را فراهم می‌ک

نند.

### عملکرد

- **Refresh Serial Ports:** با کلیک بر روی دکمه "Refresh Serial Ports"، برنامه پورت‌های سریال موجود را با استفاده از ماژول `serial.tools.list_ports` استعلام کرده و نمایش می‌دهد.
- **Connect to Arduino:** با کلیک بر روی دکمه "Connect" ارتباط با پورت Arduino مشخص شده برقرار می‌شود و `SerialThread` برای دریافت مداوم داده شروع می‌شود.

### کلاس SerialThread

- **عملیات همروند:** از QThread PyQt برای انجام وظایف همزمان با نخ اصلی برنامه استفاده می‌کند.
- **دریافت داده:** پورت سریال را برای داده‌های ورودی نظارت می‌کند و زمانی که داده دریافت می‌شود، pyqtSignal (`data_received`) را ارسال می‌کند.
- **Stop Thread:** یک متد (`stop_thread`) را پیاده‌سازی کرده است تا نخ را به آرامی متوقف کند.

## اجرای برنامه

برای اجرای برنامه، دستورات موجود در بخش "استفاده" این README را دنبال کنید.

## نمایه شماتیک

![نمایه شماتیک](/Shematic.png)

## ویدئوی نمایش پروژه

[تماشای ویدئوی نمایش پروژه](لینک_به_ویدئو_نمایش)
