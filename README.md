# django_channels_test
Quick demo environment for django channels chat with public chatrooms

Created in 4 hours.

Requires:
* functional docker-compose

Installation: pull & docker-compose up in the folder
(Builds MySQL, Redis & Django Core)

Test superuser: test / pass: test

Functionalities:
- Create product(through admin)
- Anonymous real-time chat with product owner(session based)
- Image & Video Upload
- Syncronous message notification
- No cosmetics, no js other than websockets

Default Homepage: localhost:8000/
- Product Listings & Message Product Owner functionality
- View messages functionality
- Create/join custom chatroom functionality through /chat/api (Anonymous users supported if navigated after visiting homepage)

P.S: Make sure the line separators are UNIX/MAC based(LF, "\n") for x.sh files if you copy/paste.
