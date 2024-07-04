<template>
  <div class="container-fluid my-auto">
    <div class="card" style="margin-left: auto; margin-right: auto; width: 500px">
      <div class="card-body">
        <h5 class="card-title">Изменение пароля</h5>
        <div class="card-text">
          <div class="mb-3">
            <div class="col-sm-10">
              <label for="inputPassword3" class="col-form-label">Введите новый пароль</label>
              <input type="password" v-bind:class="GetPasswordClass()" id="inputPassword3" v-model="password" />
              <div v-if="password.length !== 0 && password.length < 8" class="invalid-feedback">
                От 8 до 20 символов
              </div>
              <div v-if="password.length !== 0 && password.length >= 8" class="valid-feedback">
                От 8 до 20 символов
              </div>
            </div>
            <div v-if="password.length === 0" id="textHelp" class="form-text">
              От 8 до 20 символов
            </div>
          </div>
          <div class="mb-3">
            <div class="col-sm-10">
              <label for="inputPassword3" class="col-form-label">Повторите пароль</label>
              <input type="password" v-bind:class="GetRepeatPasswordClass()" id="inputPassword3"
                v-model="repeatPassword" />
              <div v-if="repeatPassword != '' && repeatPassword != password" id="validationServerPasswordFeedback"
                class="invalid-feedback">
                Пароль отличается!
              </div>
              <div v-if="repeatPassword != '' && repeatPassword == password" id="validationServerPasswordFeedback"
                class="valid-feedback">
                Всё отлично!
              </div>
            </div>
          </div>
          <div v-if="error == true" class="alert alert-danger d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:">
              <use xlink:href="#exclamation-triangle-fill" />
            </svg>
            <div>ОШИБКА! Введите заново пароль!</div>
          </div>
          <button type="submit" class="btn btn-primary" @click="ChangePassword">
            Подтвердить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      password: "",
      repeatPassword: "",
      error: false,
      user: "",
      user_: {},
    };
  },
  async created() {
    let jwt = this.getCookie('jwt');
    const response = await axios.get(this.base_backend_url + "/user", {
      headers: {
        Authorization: jwt,
        "Access-Control-Allow-Origin": this.access_origin,
        "Access-Control-Allow-Credentials": true,
      },
    });
    console.log(response.data.user)
    if (!(response.data.user["username"] === undefined || response.data.user["username"] == null)) {
      this.user_ = response.data.user;
      if (this.user_ == null) {
        this.user_ = undefined;
      }
    }

  },
  methods: {
    ChangePassword() {
      let canBeAuthorized = true;
      if (this.repeatPassword !== this.password) {
        canBeAuthorized = false;
      }
      if (this.password.length < 8) {
        canBeAuthorized = false;
      }

      if (canBeAuthorized == true) {
        //this.user = JSON.parse(localStorage.getItem("user"));
        //this.user = { username: "Sergey", password: "12345678"}

        axios({
          method: "put",
          url: this.base_backend_url + "/reset_password",
          data: {
            user: this.user_,
            newPassword: this.password,
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
            console.log("Вы изменили пароль!");

            //localStorage.removeItem("jwt");
            //localStorage.removeItem("user");
            //localStorage.setItem("user", JSON.stringify(response.data.user));
            //localStorage.setItem("jwt", response.data.token);
            if (localStorage.getItem("jwt") !== null) {
              //document.cookie = "jwt=" + "Bearer " + localStorage.getItem('jwt') + "; ";
              // + this.domain_clio;
              //this.$emit("loggedIn");
              console.log(document.cookie);
              this.$router.push("/cabinet");
            }
            //this.$router.push("/user");
          });
      } else {
        this.error = true;
        console.log(1);
      }
    },
    GetPasswordClass() {
      if (this.password.length == 0) {
        return "form-control";
      }
      if (this.password.length >= 8) {
        return "form-control is-valid";
      } else {
        return "form-control is-invalid";
      }
    },
    GetRepeatPasswordClass() {
      if (this.repeatPassword == "") {
        return "form-control";
      }
      if (this.repeatPassword == this.password) {
        return "form-control is-valid";
      } else {
        return "form-control is-invalid";
      }
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

<script setup>
import axios from "axios";
</script>