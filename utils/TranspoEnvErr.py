
    # initializing error list
errortranspo_list = ['Did not see screen (IAS02SHEADER) when expected; cannot continue - saw (IAS02SOVERLAY)' , 'com.expd.test.transportation.glue.legacy.exceptions.ScreenReplayException' , 'com.expd.test.transportation.glue.legacy.exceptions.ScreenLoopTimeoutException' ,
    '[ic_No] does not match actual value of []', 'com.expd.test.transportation.glue.legacy.exceptions.SessionFailureException']
test_string = "Blah blah blah this is a test string"
    # printing original string
print("The original error : " + test_string)

    # printing original list
print("The transportation environment list : " + str(errortranspo_list))

    # using list comprehension
    # checking if string contains list element
restrans = any(ele in test_string for ele in errortranspo_list)

print("Is error likely transportation environment related : " + str(restrans) )

if restrans == False :
            erroracct_list = ['Expected value [N3] in data map for screen field [TC_v001] does not match actual value of [S]']

            # printing original list
            print("The accounting error list : " + str(erroracct_list))

             # using list comprehension
            # checking if string contains list element
            resacct = any(ele in test_string for ele in erroracct_list)

            print("Is error likely accounting environment related : " + str(resacct) )
