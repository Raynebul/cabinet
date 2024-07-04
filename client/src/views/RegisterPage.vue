<template>
    <div v-if="isRegister == false" class="container-fluid my-auto">
      <div class="col-8 mx-auto">
        <div class="card justify-content-center">
          <div class="card-body">
            <h5 class="card-title">Регистрация пользователя</h5>
            <div class="card-text">
              <div class="container">
                <div class="row">
                  <div class="col">
                    <div class="mb-3">
                      <label for="inputText3" class="col-form-label"
                        >Имя пользователя<span class="text-danger">*</span></label
                      >
                      <div class="col-sm-10">
                        <input
                          type="text"
                          v-bind:class="GetUserClass()"
                          id="inputText3"
                          v-model="user.username"
                        />
                        <div
                          v-if="errorString.errno === 19"
                          class="invalid-feedback"
                        >
                          Имя пользователя должно быть уникальным
                        </div>
                        <div v-else id="textHelp" class="form-text">
                          Имя пользователя должно быть уникальным
                        </div>
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputEmail3" class="col-form-label"
                          >Почта<span class="text-danger">*</span></label
                        >
                        <input
                          type="email"
                          v-bind:class="GetEmailClass()"
                          id="inputEmail3"
                          v-model="user.email"
                        />
                        <div
                          v-if="
                            user.email.length != 0 &&
                            user.email.indexOf('@') == -1
                          "
                          class="invalid-feedback"
                        >
                          Введите почту
                        </div>
                        <div
                          v-if="
                            user.email.length != 0 &&
                            user.email.indexOf('@') != -1
                          "
                          class="valid-feedback"
                        >
                          Введите почту
                        </div>
                      </div>
                      <div
                        v-if="user.email.length === 0"
                        id="textHelp"
                        class="form-text"
                      >
                        Введите почту
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputPassword3" class="col-form-label"
                          >Пароль<span class="text-danger">*</span></label
                        >
                        <input
                          type="password"
                          v-bind:class="GetPasswordClass()"
                          id="inputPassword3"
                          v-model="user.password"
                        />
                        <div
                          v-if="
                            user.password.length !== 0 && user.password.length < 8
                          "
                          class="invalid-feedback"
                        >
                          От 8 до 20 символов
                        </div>
                        <div
                          v-if="
                            user.password.length !== 0 &&
                            user.password.length >= 8
                          "
                          class="valid-feedback"
                        >
                          От 8 до 20 символов
                        </div>
                      </div>
                      <div
                        v-if="user.password.length === 0"
                        id="textHelp"
                        class="form-text"
                      >
                        От 8 до 20 символов
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputPasswordAgain3" class="col-form-label"
                          >Повторите пароль<span class="text-danger"
                            >*</span
                          ></label
                        >
                        <input
                          type="password"
                          v-bind:class="GetRepeatPasswordClass()"
                          id="inputPasswordAgain3"
                          v-model="repeatPassword"
                          aria-describedby="inputGroupPrepend3 validationServerPasswordFeedback"
                          required
                        />
                        <div
                          v-if="
                            repeatPassword != '' &&
                            repeatPassword != user.password
                          "
                          id="validationServerPasswordFeedback"
                          class="invalid-feedback"
                        >
                          Пароль отличается!
                        </div>
                        <div
                          v-if="
                            repeatPassword != '' &&
                            repeatPassword == user.password
                          "
                          id="validationServerPasswordFeedback"
                          class="valid-feedback"
                        >
                          Всё отлично!
                        </div>
                      </div>
                      <!--
                      <div id="textHelp" class="form-text"></div>-->
                    </div>
                  </div>
                  <div class="col">
                    <div class="mb-3">
                      <label for="inputText3" class="col-sm-6 col-form-label"
                        >Статус<span class="text-danger">*</span></label
                      >
                      <select
                        v-model="user.status"
                        class="form-select col-sm-10"
                        aria-label="Default select example"
                      >
                        <option class="col-sm-10" value="Студент" selected>
                          Студент
                        </option>
                        <option class="col-sm-10" value="Преподаватель">
                          Преподаватель
                        </option>
                      </select>
                    </div>
  
                    <div class="mb-3">
                      <label for="inputText3" class="col-sm-6 col-form-label"
                        >Фамилия<span class="text-danger">*</span></label
                      >
                      <div class="col-sm-10">
                        <input
                          type="text"
                          class="form-control"
                          id="inputText3"
                          v-model="user.last_name"
                        />
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputText3" class="col-form-label"
                          >Имя<span class="text-danger">*</span></label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="inputText3"
                          v-model="user.first_name"
                        />
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputText3" class="col-form-label"
                          >Отчество</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="inputText3"
                          v-model="user.patronymic"
                        />
                      </div>
                    </div>
                    <div class="mb-3">
                      <div class="col-sm-10">
                        <label for="inputText3" class="col-form-label"
                          >Телефон</label
                        >
                        <input
                          type="text"
                          class="form-control"
                          id="inputText3"
                          v-model="user.telephone"
                        />
                      </div>
                    </div>
                  </div>
                  <p class="text-danger" style="font-size: 0.8rem">
                    * - обязательное поле
                  </p>
                </div>
                <!-- ошибка авторизации -->
                <registerError v-if="errorId === true" />
                <!--<div>{{ errorString }}</div>-->
              </div>
  
              <!--Прочее-->
  
              <!-- ошибка -->
  
              <button type="submit" class="btn btn-primary" @click="Register()">
                Зарегистрироваться
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else style="padding-top: 10%">
      <registerSuccess />
    </div>
  </template>
  
  <style></style>
  
  <script setup>
  import axios from "axios";
  import { RouterLink } from "vue-router";
  import registerSuccess from "./registerComponents/RegisterSuccess.vue";
  import registerError from "./registerComponents/RegisterError.vue";
  //import userSchema from "./registerComponents/json/user-schema.json";
  
 // import Ajv from "ajv";
  //import ajvFormats from "ajv-formats";
  </script>
  
  <script>
  import { useRoute } from "vue-router";
  const router = useRoute();
  export default {
    data() {
      return {
        user: {
          username: "",
          email: "",
          password: "",
          active: false,
          status: "",
          first_name: "",
          last_name: "",
          patronymic: "",
          telephone: "",
          role: 6,
        },
        
        //username: "",
        //email: "",
        password: "",
        repeatPassword: "",
        id: "",
        errorId: false,
        isRegister: false,
        errorString: "", 
      };
    },
    methods: {
      Register() {
        /*
        const data = {
          username: this.username,
          email: this.email,
          password: this.password,
        }; */
        //console.log("схема", userSchema);
        let canBeAuthorized = true;
        //this.DeleteAllSpaces();
        if (this.user.username == "") {
          canBeAuthorized = false;
          console.log(1);
        }
        if (this.repeatPassword !== this.user.password) {
          canBeAuthorized = false;
          console.log(1);
        }
        if (this.user.password.length < 8 || this.user.password.length > 20) {
          canBeAuthorized = false;
          console.log(2);
        }
        if (this.user.email === "") {
          canBeAuthorized = false;
          console.log(3);
        }
        if (this.user.email.indexOf("@") == -1) {
          canBeAuthorized = false;
          console.log(4);
        }
        if (this.user.first_name == "" || this.user.last_name == "") {
          canBeAuthorized = false;
          console.log(5);
        }
        if (this.user.status == "") {
          canBeAuthorized = false;
          console.log(6);
        }
        //this.ValidationJSON();
        console.log(this.user);
  
        if (canBeAuthorized === true && this.errorId == false) {
          
          axios({
            method: "post",
            url: this.base_backend_url + "/register",
            data: {
              user: this.user,
            },
            headers: {
              "Access-Control-Allow-Origin": this.access_origin,
              "Access-Control-Allow-Credentials": true,
            },
            validateStatus: (status) => {
              return true; // I'm always returning true, you may want to do it depending on the status received
            },
          })
            .catch((error) => {})
            .then((response) => {
              
              if (response.data.test === false) {
                this.errorString = response.data.error;
                this.errorId = true;
              } else {
                this.isRegister = true;
              } 
            }); 
          this.isRegister = true;
        } else {
          this.errorId = true;
        }
      },
      GetRepeatPasswordClass() {
        if (this.repeatPassword == "") {
          return "form-control";
        }
        if (this.repeatPassword == this.user.password) {
          return "form-control is-valid";
        } else {
          return "form-control is-invalid";
        }
      },
      GetPasswordClass() {
        if (this.user.password.length == 0) {
          return "form-control";
        }
        if (this.user.password.length >= 8) {
          return "form-control is-valid";
        } else {
          return "form-control is-invalid";
        }
      },
      GetEmailClass() {
        if (this.user.email.length == 0) {
          return "form-control";
        }
        if (this.user.email.indexOf("@") != -1) {
          return "form-control is-valid";
        } else {
          return "form-control is-invalid";
        }
      },
      GetUserClass() {
        if (this.errorString.errno == 19) {
          return "form-control is-invalid";
        } else {
          return "form-control";
        }
      },
      ValidationJSON() {
        this.validJSON = true;
        this.errorString = "";
        this.errorId = false;
        const ajv = new Ajv();
        ajvFormats(ajv, { mode: "fast", formats: ["email"] });
        const validateUser = ajv.compile(userSchema);
        let checkUser = this.user;
        const validUser = validateUser(checkUser);
        console.log(this);
        if (!validUser) {
          this.validJSON = false;
          this.errorString = validateUser.errors;
          console.log(1);
        }
        if (this.validJSON === false) {
          this.errorId = true;
          //this.canBeAuthorized = false;
          console.log(2);
        }
      },
      DeleteAllSpaces() {
        let i = false;
        while (i == false) {
          i = true;
          if (this.user.password[this.user.password.length - 1] == " ") {
            console.log(1, this.user.password);
            this.user.password = this.user.password.slice(0, -1);
            console.log(1, this.user.password);
            i = false;
          }
          if (this.repeatPassword[this.repeatPassword.length - 1] == " ") {
            console.log(2, this.repeatPassword);
            this.repeatPassword = this.repeatPassword.slice(0, -1);
            console.log(2, this.repeatPassword);
            i = false;
          }
          if (this.user.username[this.user.username.length - 1] == " ") {
            console.log(3, this.user.username);
            this.user.username = this.user.username.slice(0, -1);
            console.log(3, this.user.username);
            i = false;
          }
          if (this.user.email[this.user.email.length - 1] == " ") {
            console.log(4, this.user.email);
            this.user.email = this.user.email.slice(0, -1);
            console.log(4, this.user.email);
            i = false;
          }
          if (this.user.first_name[this.user.first_name.length - 1] == " ") {
            console.log(5, this.user.first_name);
            this.user.first_name = this.user.first_name.slice(0, -1);
            console.log(5, this.user.first_name);
            i = false;
          }
          if (this.user.last_name[this.user.last_name.length - 1] == " ") {
            console.log(6, this.user.last_name);
            this.user.last_name = this.user.last_name.slice(0, -1);
            console.log(6, this.user.last_name);
            i = false;
          }
          console.log(this.user);
          i = true;
        }
      },
    },
  };
  </script>
  
  <style>
  .center-block {
    display: table;
    margin: 0 auto;
    align-items: center;
  }
  </style>
  