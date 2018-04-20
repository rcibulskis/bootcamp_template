

Vue.component('nut-chart', {
  extends: VueChartJs.Bar,
  mounted () {
  	axios.get('/bootcamp_template/default/get_data2')
    	.then(response => {
    		check = response.data
    		console.log(check);
	    	labels = Object.keys(check)
	    	ratings = Object.keys(check).map(function(key){
	    					return check[key]["Mean_Ratings"];
	    				});

	    	this.renderChart({
	      		labels:labels,
	      		datasets: [
	        		{
	          			label: 'Average Critic Score per Ratings',
	          			backgroundColor: "#6D7993",
	          			data: ratings,
	        		}

	      		]
	    }, {responsive: true, maintainAspectRatio: false})
		})
	},
});

Vue.component('pie-chart', {
  extends: VueChartJs.Bar,
  mounted () {
  	axios.get('/bootcamp_template/default/get_data3')
    	.then(response => {
    		check = response.data
    		console.log(check);
	    	labels = Object.keys(check)
	    	ratings = Object.keys(check).map(function(key){
	    					return check[key]["Mean_Ratings"];
	    				});

	    	this.renderChart({
	      		labels:labels,
	      		datasets: [
	        		{
	          			label: 'Average Critic Score per Genre',
	          			backgroundColor: "#9099A2",
	          			data: ratings,
	        		}

	      		]
	    }, {responsive: true, maintainAspectRatio: false})
		})
	},
});

Vue.component('bar-chart2', {
  extends: VueChartJs.Bar,
  mounted () {
  	axios.get('/bootcamp_template/default/get_data')
    	.then(response => {
    		check = response.data
	    	labels = Object.keys(check)
	    	global_sales = Object.keys(check).map(function(key){
	    					return check[key]['Global_Sales'];
	    				});
	    	na_sales = Object.keys(check).map(function(key){
	    					return check[key]['NA_Sales'];
	    				});

	    	this.renderChart({
	      		labels:labels,
	      		datasets: [
	        		{
	          			label: 'Global Sales in units sold',
	          			backgroundColor: "#6D7993",
	          			data: global_sales,
	        		},
	        		{
	          			label: 'North American Sales in units sold',
	          			backgroundColor: '#9099A2',
	          			data: na_sales,
	        		}

	      		]
	    }, {responsive: true, maintainAspectRatio: false})
		})
	},
});

var app = new Vue({
    el: '#main',
    data: {
        include: "True",
        style_container: {
        backgroundColor: '#D5D5D5',
        width: '80%'
    	},
    	style_container_header: {
        backgroundColor: '#D5D5D5'
    	},
    	overall_container: {
        backgroundColor: '#96858F'
    	},
    	style_graph: {
        color: 'white'
    	},
    },
});