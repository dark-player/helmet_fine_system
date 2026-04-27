# Traffic Violation Detection System
## Detects: No Helmet | Triple Riding | Overspeed

---

## YOUR PROJECT FOLDER STRUCTURE

```
traffic_challan_project/
│
├── detector.py          ← MAIN FILE - Run this for detection
├── bike_owners.py       ← Run once to create owner database
├── challan_generator.py ← Generates PDF challans
├── violation_log.py     ← Saves violations to Excel
├── email_sender.py      ← Sends emails with PDF
├── send_emails.py       ← Manual email sender
├── requirements.txt     ← All packages needed
│
├── bike_owners.xlsx     ← Owner database (auto created)
├── violations.xlsx      ← All violations log (auto created)
│
├── violation_images/    ← Evidence photos saved here
├── challans/            ← PDF challans saved here
└── models/              ← (for future YOLO models)
```

---

## STEP 1 - Install packages

Open VS Code Terminal and run:

```
pip install opencv-python openpyxl fpdf2 pillow numpy
```

---

## STEP 2 - Create owner database

```
python bike_owners.py
```

This creates `bike_owners.xlsx` with 10 sample owners.
You can add more rows to this Excel file anytime.

---

## STEP 3 - Run detection

For WEBCAM:
```
python detector.py
```

For VIDEO FILE:
- Open detector.py
- Change line: `VIDEO_SOURCE = 0`
- To:          `VIDEO_SOURCE = "your_video.mp4"`
- Then run: `python detector.py`

---

## STEP 4 - Send emails (manual)

After detection is done:
1. Open `email_sender.py`
2. Change `SENDER_EMAIL` to your Gmail
3. Change `SENDER_PASSWORD` to your Gmail App Password
4. Run: `python send_emails.py`

### How to get Gmail App Password:
1. Go to myaccount.google.com
2. Security → 2-Step Verification → Enable it
3. Search "App Passwords"
4. Create App Password for "Mail"
5. Copy the 16 digit password

---

## WHAT HAPPENS WHEN VIOLATION IS DETECTED

1. Red box drawn on screen around the vehicle
2. Photo saved in `violation_images/` folder
3. Record added to `violations.xlsx`
4. PDF challan generated in `challans/` folder
5. Email sent to owner (if enabled)

---

## VIOLATION FINE AMOUNTS

| Violation               | Fine    |
|------------------------|---------|
| No Helmet               | Rs 1000 |
| Triple Riding           | Rs 1000 |
| Overspeed               | Rs 2000 |
| No Helmet + Triple      | Rs 2000 |
| No Helmet + Overspeed   | Rs 3000 |
| Triple + Overspeed      | Rs 3000 |
| All Three               | Rs 4000 |

---

## KEYBOARD CONTROLS (during detection)

| Key | Action         |
|-----|----------------|
| Q   | Quit / Stop    |
| S   | Skip frame     |

---

## TIPS FOR SLOW PC (4GB RAM)

- In detector.py, change `PROCESS_EVERY_N = 3` to `5` or `6`
- Use 480p video instead of 1080p for faster processing
- Close other applications while running detection
- Use a smaller video file for testing first

---

## HOW TO ADD YOUR OWN VIDEO

1. Copy your .mp4 file into the project folder
2. Open detector.py
3. Find this line: `VIDEO_SOURCE = 0`
4. Change to: `VIDEO_SOURCE = "your_video_name.mp4"`
5. Run: python detector.py

---

## HOW TO ADD MORE BIKE OWNERS

1. Open `bike_owners.xlsx`
2. Add new rows with:
   - Number Plate (exact format: MH12AB1234)
   - Owner Name
   - Phone
   - Email
   - Address
   - City
   - State
3. Save the file
4. Run detection again - it will use the new data

---

Made for: Final Year / Internship Project Demo
System: Windows 10 | Python 3.x | CPU only | 4GB RAM
