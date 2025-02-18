'''
Problem id: 1012-F
Statement: Gleb is a famous competitive programming teacher from Innopolis. He is planning a trip to N programming camps in the nearest future. Each camp will be held in a different country. For each of them, Gleb needs to apply for a visa. 

For each of these trips Gleb knows three integers: the number of the first day of the trip si, the length of the trip in days leni, and the number of days ti this country's consulate will take to process a visa application and stick a visa in a passport. Gleb has P (1 ≤ P ≤ 2) valid passports and is able to decide which visa he wants to put in which passport.

For each trip, Gleb will have a flight to that country early in the morning of the day si and will return back late in the evening of the day si + leni - 1.

To apply for a visa on the day d, Gleb needs to be in Innopolis in the middle of this day. So he can't apply for a visa while he is on a trip, including the first and the last days. If a trip starts the next day after the end of the other one, Gleb can't apply for a visa between them as well. The earliest Gleb can apply for a visa is day 1.

After applying for a visa of country i on day d, Gleb will get his passport back in the middle of the day d + ti. Consulates use delivery services, so Gleb can get his passport back even if he is not in Innopolis on this day. Gleb can apply for another visa on the same day he received his passport back, if he is in Innopolis this day. 

Gleb will not be able to start his trip on day si if he doesn't has a passport with a visa for the corresponding country in the morning of day si. In particular, the passport should not be in another country's consulate for visa processing.

Help Gleb to decide which visas he needs to receive in which passport, and when he should apply for each visa. 

In the first line of the input there are two integers N (1 ≤ N ≤ 22) and P (1 ≤ P ≤ 2)—the number of trips and the number of passports Gleb has, respectively.

The next N lines describe Gleb's trips. Each line contains three positive integers si, leni, ti (1 ≤ si, leni, ti ≤ 109)—the first day of the trip, the length of the trip and number of days the consulate of this country needs to process a visa application. It is guaranteed that no two trips intersect.

If it is impossible to get all visas on time, just print "NO" (quotes for clarity). Otherwise, print "YES" and N lines describing trips. For each trip, first print number of the passport Gleb should put this country's visa in, and then print number of the day he should apply for it. Print trips in the same order as they appear in the input. Days are numbered from 1, starting with tomorrow—the first day you can apply for a visa. Passports are numbered from 1 to P.

If there are several possible answers, print any of them.

Examples with answer "YES" are depicted below.

Each cell of the stripe represents a single day. Rectangles represent trips, each trip starts in the morning and ends in the evening. Rectangles with angled corners represent visa applications. Each application starts in the middle of a day and ends ti days after. The trip and the visa application for the same country have the same color.

In examples with two passports, visa applications and trips depicted above the time stripe are made using the first passport, visa applications and trips depicted below the time stripe are made using the second passport.

Example 1: 

Example 2: 

Example 3: 
Tags: dp,implementation,*3400
'''

def can_schedule_visas(N, P, trips):
    # Sort trips by their start date
    trips.sort()
    
    # Prepare result storage
    result = [None] * N  # Each entry will be a (passport_num, apply_day)
    
    # This will track the next available day for each passport
    passport_next_available = [0] * P
    
    for index, (si, leni, ti) in enumerate(trips):
        # We need to find a passport and a day to apply such that:
        # 1. The passport is free for visa application
        # 2. The visa will be ready by day `si`
        # 3. We apply on a day when Gleb is in Innopolis
        
        found = False
        for passport in range(P):
            # Check from day 1 to `si - ti`
            # Passport must be free until `si`; apply on a day in Innopolis
            for day in range(1, si - ti + 1):
                # Check if passport is available for application
                if passport_next_available[passport] <= day:
                    # Check if we can get back the visa before the trip
                    if day + ti <= si:
                        # It's possible to schedule this visa application!
                        result[index] = (passport + 1, day)
                        passport_next_available[passport] = si + leni - 1
                        found = True
                        break
            if found:
                break

        if not found:
            return False, None
    
    return True, result

# Example test case:
N = 2
P = 1
trips = [
    (10, 5, 2),  # Trip 1: starts at day 10, lasts 5 days, visa takes 2 days to process
    (20, 3, 1)   # Trip 2: starts at day 20, lasts 3 days, visa takes 1 day to process
]

expected = True
output, schedule = can_schedule_visas(N, P, trips)

# Verification
def verify():
    
    if output != expected:
        print(f"Mismatch in possibility: Expected {expected}, got {output}")
        return
    
    if output:  # Only verify the schedule if possible
        current_day = 0
        passports_available = [0] * P
        for trip_index, (passport_id, apply_day) in enumerate(schedule):
            
            si, leni, ti = trips[trip_index]
 
            # Check if we applied within proper days
            if apply_day >= si or apply_day + ti > si:
                print(f"Application day for trip {trip_index + 1} is invalid, applied {apply_day}, trip starts {si}")
                return
            
            # Ensure passport was not used on apply_day
            if apply_day < passports_available[passport_id - 1]:
                print(f"Passport {passport_id} was not available on day {apply_day} for trip {trip_index + 1}")
                return

            # Update passport availability from the end of this trip
            passports_available[passport_id - 1] = si + leni - 1

    print("Verified")

verify()