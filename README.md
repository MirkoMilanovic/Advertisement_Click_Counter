# Addvertisement click counter

This API access the data from the database and returns the following information: Given a campaign, the API returns the amount of clicks that were made on advertisements that belong to this campaign. One entry in the database represents one click.

- Eg.: for the campaign 4510461 the API should return 13.
  This API is extended by a time filter, so that it only returns the number of clicks that fall between a given start date and a given end date. Both dates are passed as a string of the format „yyyy-mm-dd hh:mm:ss“ (UTC).
- Eg.: for campaign 4510461, start date 2021-11-07 03:10:00 and end date 2021-11-07 03:30:00, the API returns 4.

## RESOURCE METHOD CHART:

| Resource          | Method | Path       | Parameter     | Status on error           |
| ----------------- | ------ | ---------- | ------------- | ------------------------- |
| getClicks         | POST   | /click     | Campaign: Int | 200: OK                   |
|                   |        |            |               | 301: Incorrect parameters |
|                   |        |            |               | 302: Incorrect values     |
|                   |        |            |               |                           |
| getClicksTimespan | POST   | /clickTime | Campaign: Int | 200: OK                   |
|                   |        |            | Start: String | 301: Incorrect parameters |
|                   |        |            | End: String   | 302: Incorrect values     |

### Tests - pytest

There is a separate "tests" folder with test scripts, that can be run with pytest

### Requirements:

Django==4.0.3
djangorestframework==3.13.1
django-cors-headers==3.11.0
pytest==7.1.1
pytest-django==4.5.2
