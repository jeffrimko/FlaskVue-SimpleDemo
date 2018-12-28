new Vue({
    el: '#app',
    data: {
        name: ''
    },
    methods: {
        gotoUser: function(event) {
            window.location.href = "/user?name=" + this.name;
        }
    }
});
