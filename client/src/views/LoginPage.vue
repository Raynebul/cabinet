<template>
  <div class="container-fluid my-auto" style="">
    <!--style="padding-top: 100px" align-items-center-->
    <!---->
    <div class="col-6 mx-auto" style="width: 40%">
      <div class="card justify-content-center">
        <div class="card-body">
          <h5 class="card-title">Вход</h5>
          <div class="card-text">
            <div class="mb-3">
              <div class="col-sm-10 form-floating">
                <!--<label for="inputText3" class="col-form-label">Логин</label>-->
                <input type="text" class="form-control" id="floatingInput" v-model="login"
                  placeholder="name@example.com" />
                <label for="floatingInput">Логин</label>
              </div>
              <!--
                <div id="textHelp" class="form-text">
                  Введите никнейм или почту
                </div>-->
            </div>
            <div class="mb-3">
              <div class="col-sm-10 form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password"
                  v-model="password" />
                <label for="floatingPassword">Пароль</label>
              </div>
              <div id="textHelp" class="form-text">От 8 до 20 символов</div>
            </div>
            <div v-if="error == true" class="alert alert-danger d-flex align-items-center" role="alert">
              <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:">
                <use xlink:href="#exclamation-triangle-fill" />
              </svg>
              <div>ОШИБКА! Неправильный логин или пароль!</div>
            </div>
            <div v-if="active == false" class="alert alert-warning d-flex align-items-center" role="alert">
              <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Warning:">
                <use xlink:href="#exclamation-triangle-fill" />
              </svg>
              <div>
                Аккаунт не активирован! Попросите оператора его активировать.
              </div>
            </div>
            <button type="submit" class="btn btn-primary" @click="Login()">
              Войти
            </button>
            <!--
            <button class="btn btn-primary" @click="eraseAllCookies">Тест</button>-->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import axios from "axios";
</script>

<script>
export default {
  data() {
    //SetCookies();
    
    //document.cookie = "jwt=1234567890; domain=.clio.ws; path=/;"
    return {
      login: "",
      password: "",
      error: false,
      active: true,
    };
  },
  mounted() {
    console.log("aaawkekwe")
    /*
    document.cookie = "jwt=123;";
    document.cookie = "jwt=123; path=/;";
    document.cookie = "jwt=123; domain=.clio.ws; path=/;";
    document.cookie = "jwt=123; domain=clio.ws; path=/;";*/
    //this.SetCookies()
  },
  methods: {
    Login() {
      console.log("wlkeoawekohwnekowhqeoh")
      axios({
        method: "post",
        url: this.base_backend_url + "/user",
        data: {
          password: this.password,
          login: this.login,
        },
        headers: {
          "Access-Control-Allow-Origin": this.access_origin,
          "Access-Control-Allow-Credentials": true,
        },
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      })
        .catch((error) => { })
        .then((response) => {
          if (response.data.error !== true) {
            console.log(response);
            console.log(this.base_url);
            let user = response.data.user;
            let token = response.data.access_token
            let refresh_token = response.data.refresh_token;
            delete user["password"]
            console.log(user, token, refresh_token, response.data.response);
            if (user !== null) {
              if (user.active === true) {
                //localStorage.setItem("user", JSON.stringify(response.data.user));
                localStorage.setItem("jwt", token);
                if (localStorage.getItem("jwt") != null) {
                  this.eraseAllCookies()
                  document.cookie = "jwt=" + "Bearer " + localStorage.getItem('jwt') + "; "
                  // + this.domain_clio;
                  this.$emit("loggedIn");
                  this.$router.push("/cabinet");
                  /*
                  axios.get(this.base_backend_url + "/user/set_cookies", {
                    headers: {
                      Authorization: 'Bearer ' + localStorage.getItem('jwt'),
                      "Access-Control-Allow-Origin": "*",
                    },
                    withCredentials: true,
                  }).then((response_cookies) => {
                    console.log("response ", response_cookies)
                    this.$emit("loggedIn");
                    this.$router.push("/user");
                    //setTimeout(() => this.$router.go("/user"), 1000);
                    //this.$router.go("/user");
                    console.log("проверка...")
                  }) */
                }
                console.log("Активирован!");
              } else {
                console.log("Неактивирован!");

                this.active = false;
              }
            } else {
              this.error = true;
            }
          }
          else {
            this.error = true;
          }
        });
      //this.isRegister = true;
    },
    SetCookies() {
      console.log("aaaaaaaa")
      document.cookie = "jwt=1234567890; domain=.clio.ws; path=/;"
    },
    eraseCookie(name) {
      console.log(document.cookie)
      console.log(name + '=' + this.getCookie('jwt') + ';' + ' expires=Thu, 01 Jan 1970 00:00:00 GMT; ' + this.domain_clio)
      document.cookie = name + '=' + ';' + ' expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + this.domain_clio;
      console.log(document.cookie)
    },
    eraseAllCookies() {
      console.log("Стирание лишних куки!")
      document.cookie = "jwt=; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
      document.cookie = "jwt=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
      document.cookie = "jwt=; domain=.clio.ws; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
      document.cookie = "jwt=; domain=clio.ws; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT;";
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
    },
    Test() {
      //let d = new Date()
      //document.cookie = 'last_visit' + "=" + d + ";" + " path=/"
      //let ca = document.cookie.split(';');
      document.cookie = "user=John"; // обновляем только куки с именем 'user'
      console.log(document.cookie); // показываем все куки
      //console.log(ca)
      /*
      axios({
        method: "post",
        url: this.base_backend_url + "/",
        data: {
        },
        headers: {
          //"Access-Control-Allow-Origin": "*",
        },
        withCredentials: true,
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      })
        .catch((error) => { })
        .then((response) => {
          console.log(response.data.message);
          console.log(this.base_url);
        });
        */
    }
  },
};
</script>

<style></style>