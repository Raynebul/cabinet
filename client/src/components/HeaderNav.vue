<script setup>
import { RouterLink, useRoute } from "vue-router";
import axios from "axios";

</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid" style="margin-left: 10px">
      <a class="navbar-brand" :href="base_frontend_url + `/`"><img src="../assets/s-logo.png" alt="" width="20"
          height="20" style="margin-left: -10px" /></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03"
        aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation"
        style="margin-right: 10px">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        </ul>
        <hr class="hr text-light" style="margin: 0 10px 0 0" />
        <ul class="navbar-nav ms-auto">
          <li class="nav-item" v-if="user === undefined">
            <RouterLink to="/login" class="nav-link" tabindex="-1">Вход</RouterLink>
          </li>
          <li class="nav-item dropdown" v-if="user !== undefined">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
              aria-expanded="false">
              {{ user.username }}
            </a>
            <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDropdown"
              style="right: 0; left: auto; /* added */">
              <li>
                <RouterLink to="/cabinet" class="dropdown-item">Профиль</RouterLink>
              </li>
              <li>
                <hr class="dropdown-divider" />
              </li>
              <li>
                <a class="dropdown-item text-danger" @click="LogOut()">Выйти</a>
              </li>
            </ul>
          </li>
          <li class="nav-item" v-if="user === undefined">
            <RouterLink to="/register" class="nav-link">Регистрация</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <LogIn />
</template>

<style></style>

<script>
export default {
  data() {
    return {
      id: "",
      user: undefined,
      route: undefined,
    };
  },

  async created() {
    let jwt = this.getCookie('jwt');
    const response = await axios.get(this.base_backend_url + "/user", {
      headers: {
        //Authorization: "Bearer " + localStorage.getItem("jwt"),
        Authorization: jwt,
        "Access-Control-Allow-Origin": this.access_origin,
        "Access-Control-Allow-Credentials": true,
      },
      //withCredentials: true,
    });
    console.log(response.data.user)
    if (!(response.data.user["username"] === undefined || response.data.user["username"] == null)) {
      this.user = response.data.user;
      if (this.user == null) {
        this.user = undefined;
      }
    }

  },
  mounted() {

    this.route = useRoute();
  },
  methods: {

    LogOut() {
      this.eraseCookie('jwt');
      console.log("Имя роута", this.route.path);
      localStorage.removeItem("jwt");
      //localStorage.removeItem("user");

      if (this.route.path == "/") {
        window.location.reload();
      } else {
        this.$router.push("/");
      }
      /*
      axios.get(this.base_backend_url + '/user/delete_cookies', {
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
        withCredentials: true,
      }).then((response) => {
        if (this.route.path == "/") {
          console.log(1)
          window.location.reload();
        } else {
          console.log(1)
          this.$router.push("/");
        }
      }) */
      /*
      if (this.route.path == "/") {
        console.log(1)
        window.location.reload();
      } else {
        console.log(1)
        this.$router.push("/");
      }*/
    },
    eraseCookie(name) {
      //console.log(document.cookie)
      //console.log(name + '=' + this.getCookie('jwt') + ';' + ' expires=Thu, 01 Jan 1970 00:00:00 GMT; ' + this.domain_clio)
      document.cookie = name + '=' + ';' + ' expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;';
      // + this.domain_clio;
      console.log(document.cookie)
    },
    getCookie(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(';');
      for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
        }
      }
      return "";
    }
  },
};
</script>
