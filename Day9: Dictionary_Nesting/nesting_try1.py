capitals = {
     "France" : "Paris",
     "Germany" :  "Berlin",
}

#Nesting a list in a dictionary
Travel_log = {
    "France"  :["Paris", "lille", "Dijon"],
    "Germany": [ "Berlin", "Hamburg", "Stuttgart"],
}

Travel_log_1 = { 
    "France" : {"cities_visited" : ["Paris", "lille", "Dijon"], "total_visits": 12},
     "Germany":{ "cities_visited" :  ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 23}
}

Travel_log_2 = [
    {
         "Country": "France",
         "cities_visited" : ["Paris", "lille", "Dijon"],
         "total_visits" : 5,
    },
    { 
         "Country": "France",
         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
         "total_visits" : 23,
    }
]
