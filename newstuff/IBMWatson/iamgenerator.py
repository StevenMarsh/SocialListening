
curl -k -X POST \
--header "Content-Type: application/x-www-form-urlencoded" \
--header "Accept: application/json" \
--data-urlencode "grant_type=urn:ibm:params:oauth:grant-type:apikey" \
--data-urlencode "apikey=oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7" \
"https://iam.cloud.ibm.com/identity/token"

#"https://iam.bluemix.net/identity/token"

curl -X POST -u "apikey:{oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7}" \
--header "Content-Type: application/json" \
--data-binary @{/Users/Will/Downloads}tone.json \
"{https://gateway.watsonplatform.net/tone-analyzer/api}/v3/tone?version=2017-09-21"

curl -X GET -u "apikey:{G3-zLu6aVw7m4rGiMZ1-QiPFKFeeIRedu7GeYFWaRmQG}" \
"{https://gateway.watsonplatform.net/tone-analyzer/api}/v3/tone?version=2017-09-21 &text=Team%2C%20I%20know%20that%20times%20are%20tough%21%20Product%20sales%20have%20been%20disappointing%20for%20the%20past%20three%20quarters.%20We%20have%20a%20competitive%20product%2C%20but%20we%20need%20to%20do%20a%20better%20job%20of%20selling%20it%21"