<script setup>
import axios from "axios";
import { RouterLink } from "vue-router";
import Toast from "./Toast.vue";

import ProfileEdit from "./ProfileEdit.vue"
//import userSchema from "../../../components/json/user-schema.json";

//import Ajv from "ajv";
//import ajvFormats from "ajv-formats";
</script>

<template>
  <div class="card shadow-sm">
    <div class="card-body">
      <div class="card">
        <div class="card-body">
          <div class="card-text">
            <div class="d-flex datas">
              <div>Никнейм</div>
              <div class="ms-auto">{{ user.username }}</div>
            </div>
            <div class="d-flex datas">
              <div>ФИО</div>
              <div class="ms-auto">
                {{ user.last_name }} {{ user.first_name }} {{ user.patronymic }}
                <!--
                <input
                  class="form-control form-control-sm name-control ms-auto text-end"
                  type="text"
                  placeholder="Имя"
                  aria-label=".form-control-sm example"
                  v-model="profile.first_name"
                />-->
              </div>
            </div>
            <div class="d-flex datas">
              <div>Почта</div>
              <div class="ms-auto">{{ user.email }}</div>
            </div>
            <div class="d-flex datas">
              <div>Роль</div>
              <div class="ms-auto">{{ role.name }}</div>
            </div>
            <div class="d-flex datas">
              <div>Должность</div>
              <div class="ms-auto">{{ user.status }}</div>
            </div>
            <div class="d-flex datas">
              <div>Телефон</div>
              <div v-if="user.telephone != ``" class="ms-auto">
                +{{ user.telephone }}
              </div>
            </div>
            <div class="d-flex datas">
              <div>Пароль</div>
              <div class="ms-auto">******</div>
            </div>
          </div>
          <!--
          <div v-else class="card-text">
            <div class="d-flex datas">
              <div>Никнейм</div>
              <input class="form-control form-control-sm ms-auto text-end" type="text" placeholder="Username"
                aria-label=".form-control-sm example" disabled v-model="profile.username" />
              
            </div>
            <div class="d-flex datas">
              <div>Фамилия</div>
              <input class="form-control form-control-sm name-control ms-auto text-end" type="text"
                placeholder="Фамилия" aria-label=".form-control-sm example" v-model="profile.last_name" />
            </div>
            <div class="d-flex datas">
              <div>Имя</div>
              <input class="form-control form-control-sm name-control ms-auto text-end" type="text" placeholder="Имя"
                aria-label=".form-control-sm example" v-model="profile.first_name" />
            </div>
            <div class="d-flex datas">
              <div>Отчество</div>
              <input class="form-control form-control-sm name-control ms-auto text-end" type="text"
                placeholder="Отчество" aria-label=".form-control-sm example" v-model="profile.patronymic" />
            </div>
            <div class="d-flex datas">
              <div>Почта</div>
              <input class="form-control form-control-sm ms-auto text-end" type="text" placeholder="Почта"
                aria-label=".form-control-sm example" v-model="profile.email" />
            </div>
            <div class="d-flex datas">
              <div>Должность</div>
              <select v-model="profile.status" class="form-select form-select-sm ms-auto text-end"
                aria-label=".form-select-sm example">
                <option value="Студент">Студент</option>
                <option value="Преподаватель">Преподаватель</option>
              </select>

            </div>
            <div class="d-flex datas">
              <div>Телефон</div>

              <input class="form-control form-control-sm ms-auto text-end" type="text" placeholder="Телефон"
                aria-label=".form-control-sm example" v-model="profile.telephone" />
            </div>
            <div class="d-flex datas">
              <div>Пароль</div>
              <RouterLink to="/reset_password" class="btn btn-sm btn-info ms-auto">
                Сменить пароль
              </RouterLink>
              
            </div>
          </div>-->
          <div></div>
          <div class="d-grid gap-2 d-md-flex justify-content-md-end">
            <!--
            <button type="button" class="btn btn-secondary me-auto">
              Настройки
            </button>-->
            <button data-bs-toggle="modal" data-bs-target="#exampleModalEditProfile" type="button" class="btn btn-primary"
              >
              <!--@click="$emit(`changeEdit`, isEditing)"-->
              Редактировать профиль
            </button>
            <!--
            <button v-else type="button" class="btn btn-secondary" @click="CancelEditing()">
              Отменить редактирование
            </button>
            <button v-if="isEditing == true" type="button" class="btn btn-success" @click="SaveEditProfile">
              Сохранить изменения
            </button>-->
          </div>
        </div>
      </div>
    </div>
  </div>
  <ProfileEdit :user="profile" :role="role" @save="Save"></ProfileEdit>
  <Toast v-if="errorId === false" :notificationText="toastString" :color="`green`" :hideToast="hideToast"
    @hideToast="HideToast()"></Toast>
  <Toast v-else :notificationText="toastString" :color="`red`" :hideToast="hideToast" @hideToast="HideToast()"></Toast>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
      default: () => { },
    },
    role: {
      type: Object,
      required: true,
    },
    toastString: {
      type: String,
      required: true,
    },
    isEditing: {
      type: Object,
      required: true,
      default: () => { },
    },
    hideToast: Boolean,
  },
  data(props) {
    //let profile = props.user;
    //console.log(props.user, profile);
    //let edit = this.isEditing;
    //console.log(111, this.isEditing);
    // console.log("профиль", profile)
    // console.log(profile);
    let profile = props.user;
    return {
      profile,
      changePassword: false,
      newPassword: "",
      validJSON: true,
      errorId: false,
      errorString: "",
    };
  },
  mounted() {
    //this.profile = this.user;
  },
  methods: {
    HideToast() {
      this.$emit(`HideToast`);
      //this.hideToast = true;
    },
    EditProfile() {
      //this.edit = !this.edit;
      console.log("is - ", this.isEditing);
      //this.$emit(`changeEdit`, this.isEditing);
      //console.log(this.edit);
    },
    ChangePassword() {
      this.changePassword = false;
    },
    Save(profile) {
      for(let key in profile) {
        this.profile[key] = profile[key];
      }
      this.SaveEditProfile();
    },
    SaveEditProfile() {
      console.log(this.profile);
      let flag = true // this.CheckSaves()
      if (flag === true) {
        axios({
          method: "put",
          url: this.base_backend_url + "/user",
          data: {
            user: this.profile,
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
            console.log(response.data)
            let new_user = response.data.user
            if (new_user !== null) {
              localStorage.setItem("user", JSON.stringify(response.data.user));
              localStorage.setItem("jwt", response.data.token);
              if (localStorage.getItem("jwt") != null) {
                document.cookie = "jwt=" + "Bearer " + localStorage.getItem('jwt') + "; " + this.domain_clio;
                //this.$emit("loggedIn");
              }
              this.$emit(`changeEditButSaved`, this.isEditing);
              this.errorId = false;
              //this.hideToast = false;
            } else {
              this.errorId = true;
            }
            //console.log(this.user);
          });
        //console.log("SUCCESS!!!");
      } else {
        //this.errorId = true;
        //this.$emit(`catchError`);
        //console.log("NO!!");
      }
    },
    Test() {
      console.log("whaaaat");
      this.$emit(`changeEdit`, this.isEditing);
    },
    CancelEditing() {
      //this.profile = this.olduser;

      console.log("1", this.profile);
      console.log("2", this.user);
      this.$emit(`changeEdit`, this.isEditing);
    },
    ClickWhenEditing() {
      //this.hideToast = true;
      //this.editSettings = false;
    },
    ConsoleWhenKeyUp() {
      console.log("нередакт", this.user);
      console.log("нередакт", this.profile);
    },
    CheckSaves() {
      this.validJSON = true;
      this.errorString = "";
      this.errorId = false;
      const ajv = new Ajv();
      ajvFormats(ajv, { mode: "fast", formats: ["email"] });
      const validateUser = ajv.compile(userSchema);
      let checkUser = this.user;
      const validUser = validateUser(checkUser);
      if (!validUser) {
        this.validJSON = false;
        this.errorString = validateUser.errors;
        console.log(1);
      }
      if (this.validJSON === false) {
        this.errorId = true;
        //this.canBeAuthorized = false;
        return false;
      } else {
        let canSaved = true;
        if (
          this.profile.email == "" ||
          this.profile.first_name == "" ||
          this.profile.last_name == ""
        ) {
          canSaved = false;
        }
        return canSaved;
      }
    },
  },
};
</script>

<style>
.datas {
  padding-bottom: 10px;
}

.datas .form-control-sm {
  width: 10rem;
}

.datas .form-select-sm {
  width: 10rem;
}
</style>
