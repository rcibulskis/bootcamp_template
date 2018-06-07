Vue.component('bar-chart2', {
  extends: VueChartJs.Bar,
  props: ['label', 'data1', 'done'],
  watch: {
    done: function done() {
      if (this.$data._chart) {
        this.$data._chart.destroy();
      }
      this.renderChart({
        labels: this.label,
        datasets: this.data1
      }, {
        responsive: true,
        maintainAspectRatio: false
      })
    }
  },

});

var app = new Vue({
  el: '#main',
  data: {
    global_sales: [],
    na_sales: [],
    label: [],
    done: "",
    ratingslabel: [],
    criticalscore: [],
    criticscore: [],
    genrelabel: [],
    ratingsArray: [],
    genreArray: [],
    salesArray: [],
    publishers: ["Nintendo", "Sony", "Microsoft"],
    publisherselected: 'Nintendo',
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
  mounted: function () {
    this.postNow();
  },
  methods: {
    postNow: function () {
      var _this = this;
      this.done = '';
      axios.post('../default/get_data', {
          publisherselected: this.publisherselected
        })
        .then(function (response) {
          sales = response.data.sales
          ratings = response.data.ratings
          genre = response.data.genre
          var label = []
          var global_sales = []
          var na_sales = []
          var ratingslabel = []
          var criticalscore = []
          var criticscore = []
          var genrelabel = []

          for (var x in sales.global_sales) {
            label.push(x);
          }

          for (var x in label) {
            global_sales.push(sales['global_sales'][label[x]])
            na_sales.push(sales['na_sales'][label[x]])
          }

          for (var x in ratings.critic_score) {
            ratingslabel.push(x);
          }

          for (var x in ratingslabel) {
            criticalscore.push(ratings['critic_score'][ratingslabel[x]])
          }

          for (var x in genre.critic_score) {
            genrelabel.push(x);
          }

          for (var x in genrelabel) {
            criticscore.push(genre['critic_score'][genrelabel[x]])
          }

          _this.label = label
          _this.global_sales = global_sales
          _this.na_sales = na_sales
          _this.ratingslabel = ratingslabel
          _this.criticalscore = criticalscore
          _this.criticscore = criticscore
          _this.genrelabel = genrelabel

          var ratingsArray = [];
          var genreArray = [];
          var salesArray = [];

          _this.ratingsArray = [{
            label: 'Average critic score per ESRB ratings',
            backgroundColor: "#6D7993",
            data: _this.criticalscore
          }];

          _this.genreArray = [{
            label: 'Average critic score per genre',
            backgroundColor: "#6D7993",
            data: _this.criticscore
          }];

          _this.salesArray = [{
              label: 'Global Sales in units sold',
              backgroundColor: "#6D7993",
              data: _this.global_sales
            },
            {
              label: 'North America Sales in units sold',
              backgroundColor: "#9099A2",
              data: _this.na_sales
            }
          ];

          _this.done = "Done"
        });
    },
  },
  delimiters: ["<%", "%>"]
});
