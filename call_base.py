def total_cost(calls):
    final_cost = 0
    date_duration = {}
    for call in calls:
        call = call.split(" ")
        c_date = call[0] # date of the current call
        duration = int(call[2]) # duration of the current call
        duration = int(duration / 60) + (duration % 60 > 0)  #round UP duration of the call
        # sum calls for same days into the value
        if c_date not in date_duration:
            date_duration[c_date] = duration
        else:
            date_duration[c_date] += duration
    # calculating a cost of the calls 
    for key, value in date_duration.items():
        if value > 100:
            final_cost += 100+(value-100)*2
        else:
            final_cost += value
    #print(final_cost)

    return final_cost


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    print("All set? Click 'Check' to review your code and earn rewards!")
