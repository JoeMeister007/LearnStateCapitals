#a list of dictionaries
#each dictionary represents a state
#having a name, a capital, and a non-empty list of other
#major cities in the state
states = [
    {
        "name" : "Alabama",
        "capital" : "Montgomery",
        "other_cities" : ["Birmingham", "Auburn", "Huntsville"]
    },
    {
        "name" : "Alaska",
        "capital" : "Juneau",
        "other_cities" : ["Anchorage"]
    },
    {
        "name" : "Arizona",
        "capital" : "Phoenix",
        "other_cities" : ["Tucson", "Sedona", "Flagstaff"]
    },
    {
        "name" : "Arkansas",
        "capital" : "Little Rock",
        "other_cities" : ["Arkansas City", "Jonesboro"]
    },
    {
        "name" : "California",
        "capital" : "Sacramento",
        "other_cities" : ["Los Angeles", "San Francisco", "San Diego", "San Jose", "Oakland"]
    },
    {
        "name" : "Colorado",
        "capital" : "Denver",
        "other_cities" : ["Colorado Springs", "Boulder"]
    },
    {
        "name" : "Connecticut",
        "capital" : "Hartford",
        "other_cities" : ["New Haven", "Bridgeport"]
    },
    {
        "name" : "Delaware",
        "capital" : "Dover",
        "other_cities" : ["Wilmington", "Newark"]
    },
    {
        "name" : "Florida",
        "capital" : "Tallahassee",
        "other_cities" : ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale"]
    },
    {
        "name" : "Georgia",
        "capital" : "Atlanta",
        "other_cities" : ["Savannah", "Augusta", "Athens"]
    },
    {
        "name" : "Hawaii",
        "capital" : "Honolulu",
        "other_cities" : ["Kailua-Kona", "Kailua"]
    },
    {
        "name" : "Idaho",
        "capital" : "Boise",
        "other_cities" : ["Idaho Falls", "Moscow"]
    },
    {
        "name" : "Illinois",
        "capital" : "Springfield",
        "other_cities" : ["Chicago", "Illinois City", "Rockford"]
    },
    {
        "name" : "Indiana",
        "capital" : "Indianapolis",
        "other_cities" : ["Fort Wayne", "Bloomington", "South Bend"]
    },
    {
        "name" : "Iowa",
        "capital" : "Des Moines",
        "other_cities" : ["Iowa City", "Cedar Rapids", "Davenport"]
    },
    {
        "name" : "Kansas",
        "capital" : "Topeka",
        "other_cities" : ["Kansas City", "Wichita", "Emporia"]
    },
    {
        "name" : "Kentucky",
        "capital" : "Frankfort",
        "other_cities" : ["Louisville", "Lexington"]
    },
    {
        "name" : "Louisiana",
        "capital" : "Baton Rouge",
        "other_cities" : ["New Orleans", "Lafayette"]
    },
    {
        "name" : "Maine",
        "capital" : "Augusta",
        "other_cities" : ["Portland"]
    },
    {
        "name" : "Maryland",
        "capital" : "Annapolis",
        "other_cities" : ["Baltimore", "Frederick"]
    },
    {
        "name" : "Massachusetts",
        "capital" : "Boston",
        "other_cities" : ["Salem", "Cambridge", "Plymouth"]
    },
    {
        "name" : "Michigan",
        "capital" : "Lansing",
        "other_cities" : ["Detroit", "Grand Rapids", "Ann Arbor"]
    },
    {
        "name" : "Minnesota",
        "capital" : "Saint Paul",
        "other_cities" : ["Minneapolis", "Duluth"]
    },
    {
        "name" : "Mississippi",
        "capital" : "Jackson",
        "other_cities" : ["Gulfport", "Southaven"]
    },
    {
        "name" : "Missouri",
        "capital" : "Jefferson City",
        "other_cities" : ["Kansas City", "St. Louis"]
    },
    {
        "name" : "Montana",
        "capital" : "Helena",
        "other_cities" : ["Bozeman", "Great Falls"]
    },
    {
        "name" : "Nebraska",
        "capital" : "Lincoln",
        "other_cities" : ["Omaha", "Nebraska City"]
    },
    {
        "name" : "Nevada",
        "capital" : "Carson City",
        "other_cities" : ["Las Vegas", "Reno"]
    },
    {
        "name" : "New Hampshire",
        "capital" : "Concord",
        "other_cities" : ["Manchester", "Portsmouth"]
    },
    {
        "name" : "New Jersey",
        "capital" : "Trenton",
        "other_cities" : ["Jersey City", "Newark", "Atlantic City"]
    },
    {
        "name" : "New Mexico",
        "capital" : "Santa Fe",
        "other_cities" : ["Albuquerque"]
    },
    {
        "name" : "New York",
        "capital" : "Albany",
        "other_cities" : ["Buffalo", "Rochester", "New York"]
    },
    {
        "name" : "North Carolina",
        "capital" : "Raleigh",
        "other_cities" : ["Charlotte", "Wilmington", "Durham"]
    },
    {
        "name" : "North Dakota",
        "capital" : "Bismarck",
        "other_cities" : ["Fargo", "Grand Forks"]
    },
    {
        "name" : "Ohio",
        "capital" : "Columbus",
        "other_cities" : ["Cleveland", "Cincinnati", "Dayton"]
    },
    {
        "name" : "Oklahoma",
        "capital" : "Oklahoma City",
        "other_cities" : ["Tulsa", "Stillwater"]
    },
    {
        "name" : "Oregon",
        "capital" : "Salem",
        "other_cities" : ["Portland", "Eugene", "Bend"]
    },
    {
        "name" : "Pennsylvania",
        "capital" : "Harrisburg",
        "other_cities" : ["Philadelphia", "Pittsburgh", "Gettysburg"]
    },
    {
        "name" : "Rhode Island",
        "capital" : "Providence",
        "other_cities" : ["Newport", "Bristol"]
    },
    {
        "name" : "South Carolina",
        "capital" : "Columbia",
        "other_cities" : ["Charleston", "Myrtle Beach", "Gettysburg"]
    },
    {
        "name" : "South Dakota",
        "capital" : "Pierre",
        "other_cities" : ["Sioux Falls", "Rapid City"]
    },
    {
        "name" : "Tennessee",
        "capital" : "Nashville",
        "other_cities" : ["Memphis", "Knoxville"]
    },
    {
        "name" : "Texas",
        "capital" : "Austin",
        "other_cities" : ["Houston", "Dallas", "San Antonio"]
    },
    {
        "name" : "Utah",
        "capital" : "Salt Lake City",
        "other_cities" : ["Provo"]
    },
    {
        "name" : "Vermont",
        "capital" : "Montpelier",
        "other_cities" : ["Burlington", "Bennington"]
    },
    {
        "name" : "Virginia",
        "capital" : "Richmond",
        "other_cities" : ["Norfolk", "Lynchburg"]
    },
    {
        "name" : "Washington",
        "capital" : "Olympia",
        "other_cities" : ["Seattle", "Tacoma"]
    },
    {
        "name" : "West Virginia",
        "capital" : "Charleston",
        "other_cities" : ["Morgantown", "Huntington"]
    },
    {
        "name" : "Wisconsin",
        "capital" : "Madison",
        "other_cities" : ["Milwaukee", "Green Bay"]
    },
    {
        "name" : "Wyoming",
        "capital" : "Cheyenne",
        "other_cities" : ["Jackson"]
    }
]