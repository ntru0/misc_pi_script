
import os
import logging
from garminconnect import Garmin, GarminConnectAuthenticationError

# Fill in your login. Remember to keep your credentials private!!

EMAIL    = "@gmail.com"
PASSWORD = ":"


ACTIVITY_LIMIT = 10

TOKEN_STORE = os.path.expanduser("~/.garmin_tokens")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def login() -> Garmin:

    api = Garmin(EMAIL, PASSWORD, is_cn=False, return_on_mfa=False)
    try:
        
        api.login(TOKEN_STORE)
        log.info("Logged in using cached session.")
    except Exception:
        log.info("No valid cached session – logging in fresh.")
        api.login()
        api.garth.dump(TOKEN_STORE)
    return api


def set_other_str(api: Garmin) -> None:
    try:
        
        type = api.get_activity_types()[11] #strengthtraining
        
        activities = api.get_activities(0,ACTIVITY_LIMIT)
        for i in range(0, ACTIVITY_LIMIT): 
            if activities[i]['activityType']['typeKey']=='other':

                
                id = activities[i]['activityId']
                type_id = type["typeId"]
                type_key = type["typeKey"]
                parent_typeid = type.get( "parentTypeId", type["typeId"])
                result = api.set_activity_type(id, type_id, type_key, parent_typeid)
                print("activity %d: changed", id)
                return True, result, None

 

    except Exception as e:
        print(f"❌ : {e}")
        

    
def main() -> None:
    if not EMAIL or not PASSWORD:
        log.error("Set GARMIN_EMAIL and GARMIN_PASSWORD before running.")
        return

    try:
        api = login()
        set_other_str(api)
    except GarminConnectAuthenticationError:
        log.error("Authentication failed – check your email/password.")
    except Exception as exc:
        log.exception("Unexpected error: %s", exc)


if __name__ == "__main__":
    main()