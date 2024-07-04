<template>
  <!--row row-cols-auto col-->
  <div class="row me-0">
    <div class="col">
      <div class="container-fluid d-flex align-items-start min-vh-100">
        <!--class="shadow nav flex-column nav-pills me-3 min-vh-100"-->
        <!--margin-left: 50px; width: 300px;-->
        <div :class="AnotherProfileClass() + ` border-top border-secondary position-sticky`" id="v-pills-tab"
          role="tablist" aria-orientation="vertical" style="
              background-color: rgb(255, 255, 255); width: 210px;             
            ">
          <div class="text-center" style="margin-top: 25px; margin-bottom: 25px">
            <h4 class="text-light">{{ user.username }}</h4>
            <h6 class="text-light">{{ user.email }}</h6>
          </div>
          <button  style="font-size: 0.8rem;" @click="ClickNotManager(); nav = `profile`"
            class="nav-link active text-start" id="v-pills-home-tab" data-bs-toggle="pill"
            data-bs-target="#v-pills-home" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">
            <i class="bi bi-person-circle" style="padding-right: 10px"></i>Профиль
          </button>
          <button v-if="role.trainer === true" style="font-size: 0.8rem;"
            @click="ChangeEditing(); ClickNotManager(); nav = `materials`; reload_materials++;"
            class="nav-link text-start" id="v-pills-profile-tab" data-bs-toggle="pill" data-bs-target="#v-pills-profile"
            type="button" role="tab" aria-controls="v-pills-profile" aria-selected="false">
            <i class="bi bi-journals" style="padding-right: 10px"></i>Материалы
          </button>
          <button v-if="role.course === true" style="font-size: 0.8rem;" @click="ChangeEditing(); ClickNotManager(); nav = `courses`"
            class="nav-link text-start" id="v-pills-messages-tab" data-bs-toggle="pill"
            data-bs-target="#v-pills-messages" type="button" role="tab" aria-controls="v-pills-messages"
            aria-selected="false">
            <i class="bi bi-mortarboard-fill" style="padding-right: 10px"></i>Курсы
          </button>
          <button v-if="role.admin === true" style="font-size: 0.8rem;"
            @click="ChangeEditing(); ClickManager(); nav = `userlist`" class="nav-link text-start"
            id="v-pills-userlist-tab" data-bs-toggle="pill" data-bs-target="#v-pills-userlist" type="button" role="tab"
            aria-controls="v-pills-userlist" aria-selected="false">
            <i class="bi bi-people-fill" style="padding-right: 10px"></i>Менеджер пользователей
          </button>
          <!--
          <button v-if="nav === `userlist`" data-bs-toggle="modal" data-bs-target="#AddUserModal"
            style="font-size: 0.8rem;" @click="" class="nav-link text-start list-button" id="v-pills-userlist-tab">
            <i class="bi bi-plus-circle" style="padding-right: 10px; padding-left: 15px;"></i><span class=""
              style="">Добавить пользователя</span>
          </button>-->
          <button v-if="role.admin === true" style="font-size: 0.8rem;"
            @click="ChangeEditing(); ClickManager(); nav = `rolelist`" class="nav-link text-start"
            id="v-pills-rolelist-tab" data-bs-toggle="pill" data-bs-target="#v-pills-rolelist" type="button" role="tab"
            aria-controls="v-pills-rolelist" aria-selected="false">
            <i class="bi bi-person-fill-gear" style="padding-right: 10px"></i>Менеджер ролей
          </button>
          <!--
          <button v-if="nav === `rolelist`" data-bs-toggle="modal" data-bs-target="#AddRoleModal"
            style="font-size: 0.8rem;" @click="" class="nav-link text-start list-button" id="v-pills-userlist-tab">
            <i class="bi bi-plus-circle" style="padding-right: 10px;  padding-left: 15px;"></i><span class=""
              style="">Добавить роль</span>
          </button>-->
        </div>
        <div :class="ProfileClass() + ` `" id="v-pills-tabContent" :style="ProfileStyle() + ``">
          <div class="tab-block tab-pane fade show active" style="" id="v-pills-home" role="tabpanel"
            aria-labelledby="v-pills-home-tab">
            <Block :text="`Профиль`"></Block>
            <ProfilePost v-if="loaded == true" :user="user" :isEditing="isEditing" :key="reload" :hideToast="hideToast"
              @changeEdit="ChangeEdit" :role="role" @changeEditButSaved="ChangeEditButSaved" @HideToast="HideToast"
              @catchError="CatchError" :toastString="toastString"></ProfilePost>
          </div>
          <div class="tab-block tab-pane fade" id="v-pills-profile" role="tabpanel"
            aria-labelledby="v-pills-profile-tab">
            <div class="shadow-sm text-muted d-flex"
              style="background-color: white; padding-left: 10px; height: 50px; margin-bottom: 15px;">
              <h4 class="my-auto">Материалы</h4>
            </div>
            <div class="dropdown m-2">
              <button class="btn btn-info dropdown-toggle" type="button" id="dropdownMenuButton2"
                data-bs-toggle="dropdown" aria-expanded="false">
                Создать...
              </button>
              <ul class="dropdown-menu dropdown-menu-dark" style="border-radius: 0;"
                aria-labelledby="dropdownMenuButton2">
                <li><a class="dropdown-item my-1" :href="sim_frontend_url + `/constructor`"
                    @click="CreateTrainer()">тренажер</a></li>
                <li><a class="dropdown-item my-1" :href="problem_frontend_url + `/`">задачу</a></li>
                <li><a class="dropdown-item my-1" :href="question_frontend_url + `/`">вопрос</a></li>
              </ul>
            </div>
            <div class="scrollbar-primary border border-secondary pe-3" style="
                  height: 550px;
                  display: flex;
                  flex-direction: column-reverse;
                ">
              <div class="row row-cols-1 row-cols-md-4 g-4 overflow-auto" style="margin-bottom: auto; margin-top: 5px">
                <MaterialPost :reload="reload_materials" :hideToast="hideToast" @HideToast="HideToast"
                  :toastString="toastString" @saveMetadata="SaveMetadata" @deleteMaterial="DeleteMaterial"
                  v-if="loaded == true" :user="user" :materials="materials"></MaterialPost>
              </div>

            </div>
          </div>
          <div class="tab-block tab-pane fade" id="v-pills-messages" role="tabpanel"
            aria-labelledby="v-pills-messages-tab">
            <Block :text="`Курсы`"></Block>
            <button class="btn btn-info mx-2 mb-2">Создать курс</button>
            <!--
            <div class="text-muted d-flex shadow-sm" style="background-color: rgb(255, 255, 255)">
              <div class="my-auto" style="margin-left: 10px">Список</div>
              <button disabled to="/createtrainercourse" class="btn btn-info ms-auto text-light" style="
                    margin-top: 10px;
                    margin-bottom: 10px;
                    margin-right: 10px;
                  ">
                Создать курс
              </button>
            </div>-->
            <div class="scrollbar-primary" style="
                  height: 550px;
                  display: flex;
                  flex-direction: column-reverse;
                ">
              <div class="row row-cols-1 row-cols-md-3 g-4 overflow-auto" style="margin-bottom: auto; margin-top: 5px">
                <CoursePost v-if="loaded == true" :trainercourses="trainercourses"></CoursePost>
              </div>
            </div>
          </div>
          <div class="tab-block tab-pane fade border-start" id="v-pills-userlist" role="tabpanel"
            aria-labelledby="v-pills-userlist-tab" style="margin-right: 0px; width: ">
            <div class="shadow-sm text-muted d-flex"
              style="background-color: white; padding-left: 10px; height: 50px; margin-bottom: 15px;">
              <h4 class="my-auto">Менеджер пользователей</h4>
            </div>
            <button class="btn btn-info mx-2 mb-2" data-bs-toggle="modal" data-bs-target="#AddUserModal">Добавить
              пользователя</button>
            <div class="scrollbar-primary" style="
                ">
              <UserManagerPost v-if="loaded == true" :key="reload" :roles_="roles" :users_="users" @deleteUser="DeleteUser"></UserManagerPost>
            </div>
          </div>
          <div class="tab-block tab-pane fade border-start" id="v-pills-rolelist" role="tabpanel"
            aria-labelledby="v-pills-rolelist-tab" style="margin-right: 0px;">
            <div class="shadow-sm text-muted d-flex"
              style="background-color: white; padding-left: 10px; height: 50px; margin-bottom: 15px;">
              <h4 class="my-auto">Менеджер ролей</h4>
            </div>
            <button class="btn btn-info mx-2 mb-2" data-bs-toggle="modal" data-bs-target="#AddRoleModal">Добавить
              роль</button>
            <div class="scrollbar-primary" style="
                ">
              <RoleManagerPost @saveRole="SaveRole" @DeleteRole="DeleteRole" v-if="loaded == true" :key="reload"
                :roles_="roles">
              </RoleManagerPost>
            </div>
          </div>

        </div>
      </div>
    </div>
    <AddUser @AddNewUser="AddNewUser"></AddUser>
    <AddRole @AddNewRole="AddNewRole"></AddRole>
  </div>
</template>

<script setup>
import Block from "./userComponents/WhiteBlockOnUserboard.vue";
import MaterialPost from "./userComponents/MaterialPost.vue";
import CoursePost from "./userComponents/CoursePost.vue";
import ProfilePost from "./userComponents/ProfilePost.vue";

import AddUser from "./userComponents/AddUser.vue";
import AddRole from "./userComponents/AddRole.vue";

import UserManagerPost from "./userComponents/UserManagerPost.vue";
import RoleManagerPost from "./userComponents/RoleManagerPost.vue";

import axios from "axios";

import { Tooltip } from "bootstrap";
import { RouterLink } from "vue-router";
</script>

<script>
export default {
  async created() {
    let jwt = this.getCookie('jwt');
    const response = await axios.get(this.base_backend_url + "/user", {
      headers: {
        Authorization: jwt,
        "Access-Control-Allow-Origin": this.access_origin,
        "Access-Control-Allow-Credentials": true,
      },
      //withCredentials: true,
    }).catch((error) => { console.log(error) })
    //if(response != undefined)
    console.log("ммм да во", response.data.user)
    this.user = response.data.user;
    this.role = response.data.role;
  },

  data() {
    let metadata_s = [];
    let users = [];
    let roles = [];

    return {
      user: {},
      manager: false,
      role: {},
      roles,
      users,
      loaded: false,
      trainercourses: "",
      materials: [],
      toastString: "",
      isEditing: false,
      reload: 0,
      hideToast: true,
      validJSON: true,
      nav: 'profile',
      reload_materials: 0,
    };
  },

  mounted() {
    new Tooltip(document.body, {
      selector: "[data-bs-toggle='tooltip']",
    });
    this.GetAllMaterials()
    axios({
      method: "get",
      url: this.base_backend_url + "/userlist",
      headers: {
        "Access-Control-Allow-Origin": this.access_origin,
        "Access-Control-Allow-Credentials": true,
      },
      validateStatus: (status) => {
        return true; // I'm always returning true, you may want to do it depending on the status received
      },
    }).then((response) => {
      this.users = response.data.users;


      console.log('все юзеры', response.data.users);
      //rolelist
      axios({
        method: "get",
        url: this.base_backend_url + "/rolelist",
        headers: {
          "Access-Control-Allow-Origin": this.access_origin,
          "Access-Control-Allow-Credentials": true,
        },
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      }).then((response1) => {
        this.roles = response1.data.roles;
        /*
        for (let i = 0; i < 20; i++) {
          this.roles.push(this.role);
        }*/
        this.reload++;
        this.loaded = true;
        //console.log('вспе юзеры',response.data.users);
      });
    });

  },
  methods: {
    AddNewUser(user) {
      this.users.push(user);
    },
    AddNewRole(role) {
      console.log("YEEEE! 2lil3uoiu")
      this.roles.push(role);
      this.reload++;
    },
    DeleteRole(new_roles) {
      this.roles = new_roles;
      this.reload++;
    },
    DeleteMaterial(material) {
      let material_index = this.materials.findIndex((element) => element.id === material.id);
      let id = this.materials[material_index].id
      //console.log(this.materials[material_index], this.materials[material_index].id, material_index);
      axios({
        method: "delete",
        url: this.base_backend_url + "/user/material",
        data: {
          id: id,
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
          console.log("arg arg")
          this.materials.splice(material_index, 1);
          this.reload++;
        });
      if (this.materials[material_index].metadata_.type = "Тренажёр") {
        axios({
          method: "delete",
          url: this.sim_backend_url + "/user/material",
          data: {
            material: material,
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

          });
      }
    },
    DeleteUser(new_users) {
      //console.log("мммм да ну ты и мдааа")
      this.users = new_users;
      this.reload++;
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
    HideToast() {
      this.hideToast = true;
    },
    ChangeEditing() {
      this.hideToast = true;
      if (this.isEditing == true) {
        console.log("123456")
        this.loaded = false;
        this.isEditing = !this.isEditing;
        this.user = JSON.parse(localStorage.getItem("user"));
        this.reload++;
        this.loaded = true;
      }
      console.log(this.isEditing);
    },
    ClickManager() {
      this.manager = true;
      this.ProfileStyle()
      this.ProfileClass()
      this.AnotherProfileClass()
    },
    ClickNotManager() {
      this.manager = false;
      this.ProfileStyle()
      this.ProfileClass()
      this.AnotherProfileClass()
      console.log("aaaa")
    },
    ProfileStyle() {
      if (this.manager === true) {
        /* height: 700px; */
        return "margin-left: 0px; width: 84%; height: 600px; "
      }
      else {
        return "height: 700px; width: 80%; margin-left: 00px"
      }
    },
    ProfileClass() {
      if (this.manager === true) {
        return "tab-content"
      }
      else {
        return "tab-content"
      }
    },
    AnotherProfileClass() {
      /* min-vh-100 */
      if (this.manager === true) {
        return "shadow nav flex-column nav-pills me-3 min-vh-100 navbar-dark bg-dark"
      }
      else {
        return "shadow nav flex-column nav-pills me-3 min-vh-100 navbar-dark bg-dark"
      }
    },

    ChangeEdit(isEditing) {
      this.hideToast = true;
      this.loaded = false;
      this.isEditing = !isEditing;
      console.log("3", this.user);
      this.user = JSON.parse(localStorage.getItem("user"));
      /*
      if (typeof this.user.settings == "string") {
        this.user.settings = JSON.parse(this.user.settings);
      } */
      /*
        for (let i = 0; i < this.user.settings.trainercourses.length; i++) {
          if (typeof this.user.settings.trainercourses[i].course == "string") {
            this.user.settings.trainercourses[i].course = JSON.parse(
              this.user.settings.trainercourses[i].course
            );
          }
        } */
      this.reload++;
      this.loaded = true;

      //this.loaded=true;
    },
    ChangeEditButSaved(isEditing) {
      this.toastString = "Данные пользователя сохранены!"
      this.hideToast = false;
      this.isEditing = !isEditing;
    },
    CatchError() {
      this.toastString = "Данные пользователя не сохранены! Ошибка!"
      this.hideToast = false;
    },
    CreateTrainer() {
      console.log("Создаётся тренажер!")
    },
    CreateTask() {
      console.log("Создаётся задача!")
    },
    CreateQuestion() {
      console.log("Создаётся вопрос!")
    },
    GetAllMaterials() {
      //user/material
      axios({
        method: "get",
        url: this.base_backend_url + "/user/material",
        headers: {
          "Access-Control-Allow-Origin": this.access_origin,
          "Access-Control-Allow-Credentials": true,
        },
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      }).then((response) => {
        console.log("материалы аааа", response.data.materials)
        let get_materials = response.data.materials;
        for (let i = 0; i < get_materials.length; i++) {
          get_materials[i]["metadata_"] = JSON.parse(get_materials[i]["metadata_"])
        }
        //console.log("доступ к тренажёрам: ",this.role.trainer)
        if (this.role.trainer === false) {
          get_materials = get_materials.filter((object) => object.metadata_.type !== 'Тренажёр')
        }
        this.materials = get_materials;
        console.log("булубуль", this.materials.length)
        
        /*
        for (let k = 0; k < 10; k++) {
          this.materials.push({
            "id": 0,
            "IDtext": "som",
            "name": "ЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩ",
            "metadata_": {
              "id": "supply_and_demand",
              "name": "ФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФФ",
              "author": "Ray",
              "cover": "",
              "description": "",
              "created": "05.12.2023",
              "status": "В разработке",
              "type": "Тренажёр"
            }
          })
        } */
        this.loaded = true;
      });
    },
    SaveMaterials() {
      console.log(this.materials)
      /*
      let materials_ = []
      for (let i = 0; i < this.materials.length; i++) {
        materials_.push(JSON.stringify(this.materials[i]))
      }
      for (let i = 0; i < materials_.length; i++) {
        materials_[i] = JSON.parse(materials_[i])
        materials_[i].metadata_ = JSON.stringify(materials_[i].metadata_);
      }
      console.log(materials_)
      axios({
        method: "put",
        url: this.base_backend_url + "/user/materials",
        data: {
          materials: materials_,
        },
        validateStatus: (status) => {
          return true; // I'm always returning true, you may want to do it depending on the status received
        },
      })
        .catch((error) => { })
        .then((response) => {
          console.log(response.data)
        }); */
    },
    SaveMetadata(metadata, name, index) {
      for (let key in metadata) {
        this.materials[index - 1].metadata_[key] = metadata[key]
      }
      this.materials[index - 1].name = name;
      this.toastString = "Метаданные сохранены!"
      this.hideToast = false;
      console.log(this.hideToast)
    },
    SaveRole(saved_role, i) {
      for (let key in saved_role) {
        this.roles[i][key] = saved_role[key];
      }
    }
  },
};
</script>

<style>
.list-button:hover {
  background-color: #2b2c2f;
}

.profile-icon {
  margin-right: 0px;
  margin-top: 0px;
  border-color: transparent !important;
  background-color: transparent !important;
}

.profile-icon-primary:focus {
  color: #0d6efd;
}

.profile-icon-danger:focus {
  color: #dc3545;
}

.table-responsive {
  max-height: 620px;
}

.tab-block {
  margin-top: 20px;
}

.scrollbar-primary::-webkit-scrollbar {
  width: 10px;
  background-color: #f5f5f5;
}

.scrollbar-primary::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.1);
  background-color: #4285f4;
}

.scrollbar-primary {
  scrollbar-color: #4285f4 #f5f5f5;
}

.card {
  border-radius: 0;
}

.manager:hover {
  background-color: #4285f4;
  color: white;
}
</style>

<style scoped>
.nav-link {
  border-radius: 0;
}

.dropdown-item:hover {
  color: aqua
}
</style>