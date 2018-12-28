new Vue({
    el: '#app',
    data: {
        movie: '',
        movies: []
    },
    methods: {
        getName: function() {
            var urlParams = new URLSearchParams(window.location.search);
            var name = urlParams.get('name');
            return name;
        },
        loadMovies: function() {
            var name = this.getName();
            axios
                .get('/api/movies/' + escape(name))
                .then(response => (this.movies = response));
        },
        addMovie: function(event) {
            var name = this.getName();
            axios
                .post('/api/movies/' + escape(name) + '/' + escape(this.movie))
                .then(response => (this.movies = response));
            this.movie = '';
        },
        delMovie: function(event) {
            var name = this.getName();
            var movie = event.target.innerText;
            axios
                .delete('/api/movies/' + escape(name) + '/' + escape(movie))
                .then(response => (this.movies = response));
        }
    },
    beforeMount() {
        this.loadMovies();
    },
    delimiters: ['[[', ']]']
});
