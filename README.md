# Wildberries Supply Booking Bot

Automates the process of booking supply slots on Wildberries seller platform.

## Features
- Automates login using Chrome profile
- Finds available time slots
- Books slots based on configured bids
- Handles unexpected alerts
- Takes screenshots of successful bookings

## Installation
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Configure settings in `config/settings.py`
4. Run: `python main.py`

## Configuration
Edit `config/settings.py` to set:
- Chrome profile path
- Driver path
- Wildberries credentials
- Booking parameters
- Timing settings