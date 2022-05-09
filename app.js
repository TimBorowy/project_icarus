const express = require('express')
const bodyParser = require('body-parser')
const axios = require('axios')
const app = express()
const port = 3000
const plugUrl = "http://192.168.1.20/api/luPYdWuR4ZXizpsNJek6yefQLYNUprF5zkZ1BxCS/lights/18/state"

app.use(bodyParser.urlencoded({ extended: true }));

// Ratelimit
let previousTime = +new Date()

app.post('/solar', (req, res) => {

  let wattage = Object.keys(req.body)[0];
  console.log({ 'wattage': wattage, 'time': +new Date() })

  if (+new Date() > previousTime) {
    // Update plug every 15 minutes
    previousTime = +new Date() + 60000 * 15
    console.log("Update plug")

    if (wattage > 100) {
      
      axios.put(plugUrl, {
        "on": true
      }).then(function (response) {
        console.log(response.data);
      }).catch(function (error) {
        console.log(error);
      });
    } else {
      axios.put(plugUrl, {
        "on": false
      })
        .then(function (response) {
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  }

  res.end()
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})