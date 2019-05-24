var app = new Vue({
	el: "#app",
	data: {

		test: [],
		image: [],
		newArray:[],
		message: "",
		url: "",
		
	},
	created: function () {
		this.getData();
		this.cities();
	
		},
        methods: {
		getData: function () {
			var fetchConfig =
				fetch("https://api.myjson.com/bins/i8run", {
					method: "GET",
					headers: new Headers({})
				}).then(function (response) {
					if (response.ok) {
						return response.json();
					}
				}).then(function (json) {
					console.log("My json", json)

					app.test = json.list;
					console.log(app.test);
      				app.pushAnArr();
			

				})
				.catch(function (error) {
					console.log(error);
				})
		},
			
		cities: function () {
			var fetchConfig =
				fetch("https://pixabay.com/api/?key=8f46c985e7b5f885798e9a5a68d9c036&q=Iligan", {
					method: "GET",
					headers: new Headers({})
				}).then(function (response) {
					if (response.ok) {
						return response.json();
					}
				}).then(function (json) {
					console.log("My json", json)

					app.image = json.hits;
					console.log(app.image);
				

				})
				.catch(function (error) {
					console.log(error);
				})
		},
			
	 pushAnArr: function(){
		for(var i=0; i<app.test.length; i++){
			
			app.newArray.push(app.test[i].weather[0].icon);
		 
			
		}
		 			console.log(app.newArray); 

		
	 }
			
			
	}
})

 