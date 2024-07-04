<template>
    <div style="width: 100%">
        <!--
        <div class="d-flex " style="background-color: white;">
            <button @click="OpenUserForm()" class="btn btn-lg rounded-0 btn-info text-white">+</button>
            <h5 class="text-info px-4">
                <div style="padding-top: 10px;">Добавить пользователя</div>
            </h5>
        </div>-->
        <div v-if="form === true">
            <div class="col-8" style="width: 100%">
                <div class="card justify-content-center">
                    <div class="card-body">
                        <div class="card-text">
                            <div class="container">
                                <div class="row">
                                    <div class="col">
                                        <div class="mb-0">
                                            <label for="inputText3" class="col-form-label">Имя пользователя<span
                                                    class="text-danger">*</span></label>
                                            <div class="col-sm-10">
                                                <input type="text" v-bind:class="GetUserClass()" id="inputText3"
                                                    v-model="user.username" />
                                                <div v-if="errorString.errno === 19" class="invalid-feedback">
                                                    Имя пользователя должно быть уникальным
                                                </div>
                                                <div v-else id="textHelp" class="form-text">
                                                    Имя пользователя должно быть уникальным
                                                </div>
                                            </div>
                                        </div>
                                        <div class="mb-0">
                                            <div class="col-sm-10">
                                                <label for="inputEmail3" class="col-form-label">Почта<span
                                                        class="text-danger">*</span></label>
                                                <input type="email" v-bind:class="GetEmailClass()" id="inputEmail3"
                                                    v-model="user.email" />
                                                <div v-if="
                                                    user.email.length != 0 &&
                                                    user.email.indexOf('@') == -1
                                                " class="invalid-feedback">
                                                    Введите почту
                                                </div>
                                                <div v-if="
                                                    user.email.length != 0 &&
                                                    user.email.indexOf('@') != -1
                                                " class="valid-feedback">
                                                    Введите почту
                                                </div>
                                            </div>
                                            <div v-if="user.email.length === 0" id="textHelp" class="form-text">
                                                Введите почту
                                            </div>
                                        </div>
                                        <div class="mb-0">
                                            <div class="col-sm-10">
                                                <label for="inputPassword3" class="col-form-label">Пароль<span
                                                        class="text-danger">*</span></label>
                                                <input type="password" v-bind:class="GetPasswordClass()"
                                                    id="inputPassword3" v-model="user.password" />
                                                <div v-if="
                                                    user.password.length !== 0 && user.password.length < 8
                                                " class="invalid-feedback">
                                                    От 8 до 20 символов
                                                </div>
                                                <div v-if="
                                                    user.password.length !== 0 &&
                                                    user.password.length >= 8
                                                " class="valid-feedback">
                                                    От 8 до 20 символов
                                                </div>
                                            </div>
                                            <div v-if="user.password.length === 0" id="textHelp" class="form-text">
                                                От 8 до 20 символов
                                            </div>
                                        </div>
                                        <div class="mb-3">
                                            <div class="col-sm-10">
                                                <label for="inputPasswordAgain3" class="col-form-label">Повторите
                                                    пароль<span class="text-danger">*</span></label>
                                                <input type="password" v-bind:class="GetRepeatPasswordClass()"
                                                    id="inputPasswordAgain3" v-model="repeatPassword"
                                                    aria-describedby="inputGroupPrepend3 validationServerPasswordFeedback"
                                                    required />
                                                <div v-if="
                                                    repeatPassword != '' &&
                                                    repeatPassword != user.password
                                                " id="validationServerPasswordFeedback" class="invalid-feedback">
                                                    Пароль отличается!
                                                </div>
                                                <div v-if="
                                                    repeatPassword != '' &&
                                                    repeatPassword == user.password
                                                " id="validationServerPasswordFeedback" class="valid-feedback">
                                                    Всё отлично!
                                                </div>
                                            </div>
                                            <!--
                        <div id="textHelp" class="form-text"></div>-->
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="mb-0">
                                            <label for="inputText3" class="col-sm-6 col-form-label">Статус<span
                                                    class="text-danger">*</span></label>
                                            <select v-model="user.status" class="form-select col-sm-10"
                                                aria-label="Default select example">
                                                <option class="col-sm-10" value="Студент" selected>
                                                    Студент
                                                </option>
                                                <option class="col-sm-10" value="Преподаватель">
                                                    Преподаватель
                                                </option>
                                            </select>
                                        </div>

                                        <div class="mb-0">
                                            <label for="inputText3" class="col-sm-6 col-form-label">Фамилия<span
                                                    class="text-danger">*</span></label>
                                            <div class="col-sm-10">
                                                <input type="text" class="form-control" id="inputText3"
                                                    v-model="user.last_name" />
                                            </div>
                                        </div>
                                        <div class="mb-0">
                                            <div class="col-sm-10">
                                                <label for="inputText3" class="col-form-label">Имя<span
                                                        class="text-danger">*</span></label>
                                                <input type="text" class="form-control" id="inputText3"
                                                    v-model="user.first_name" />
                                            </div>
                                        </div>
                                        <div class="mb-0">
                                            <div class="col-sm-10">
                                                <label for="inputText3" class="col-form-label">Отчество</label>
                                                <input type="text" class="form-control" id="inputText3"
                                                    v-model="user.patronymic" />
                                            </div>
                                        </div>
                                        <div class="mb-0">
                                            <div class="col-sm-10">
                                                <label for="inputText3" class="col-form-label">Телефон</label>
                                                <input type="text" class="form-control" id="inputText3"
                                                    v-model="user.telephone" />
                                            </div>
                                        </div>
                                    </div>
                                    <p class="text-danger" style="font-size: 0.8rem">
                                        * - обязательное поле
                                    </p>
                                </div>
                                <!-- ошибка авторизации -->
                                <registerError v-if="errorId === true" />
                            </div>
                            <div class="container-fluid text-end">
                                <button type="submit" class="btn btn-sm btn-primary rounded-0" @click="Register()">
                                    Добавить
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="table-responsive" style="width: 100%">
            <!--background-color: white;-->
            <table class="table table-hover" style="width: 100%;">
                <thead class="table-info table-bordered">
                    <tr>
                        <th scope="col" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;"
                            class="align-middle text-center">#</th>
                        <th scope="col"
                            style="font-size: 0.8rem; padding-left: 6%; font-family: 'Varela Round', sans-serif;"
                            class="align-middle">Username</th>
                        <th scope="col"
                            style="font-size: 0.8rem; padding-left: 7%; font-family: 'Varela Round', sans-serif;"
                            class="align-middle">Email</th>
                        <th scope="col" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;"
                            class="align-middle text-start">Активность</th>
                        <th scope="col"
                            style="font-size: 0.8rem; padding-left: 5%; font-family: 'Varela Round', sans-serif;"
                            class="align-middle">Роль</th>
                        <th scope="col"
                            style="font-size: 0.8rem; padding-right: 30px; font-family: 'Varela Round', sans-serif;"
                            class="align-middle text-end">Действие</th>
                    </tr>
                </thead>
                <tbody class="table-responsive">
                    <tr class="table-row" v-for="user in users" :key="user">
                        <userBlock :key="load" :roles="roles" :user="user" @activate="ActivateUser"
                            @delete="ChooseObjectForDelete" @save="SaveUser">
                        </userBlock>
                    </tr>
                </tbody>
            </table>
        </div>
        <!--
        <div class="modal fade" v-for="index in users.length" :key="index"
            :id="`exampleModalUser` + users[index - 1].id" :ref="`UserEdit` + String(index)" tabindex="-1"
            aria-labelledby="exampleModalLabel">
            <div class="modal-dialog">
                <div class="modal-content rounded-0">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">
                            Информация о пользователе
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                            @click="edit = false;"></button>
                    </div>
                    <div class="modal-body">
                        <table class="table table-bordered table-hover" style="font-size: 0.8rem;">
                            <thead>
                                <tr>
                                    <th scope="col">Атрибут</th>
                                    <th scope="col">Значение</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row" class="align-middle">#</th>
                                    <td class="text-muted">
                                        <div>{{ users[index - 1].id }}</div>
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Username</th>
                                    <td class="text-muted">{{ users[index - 1].username }}</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Email</th>
                                    <td class="text-muted">{{ users[index - 1].email }}</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Пароль</th>
                                    <td class="text-muted">{{ users[index - 1].password }}</td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Роль</th>
                                    <td>
                                        <div class="text-muted" v-if="edit === false">{{ user_roles[index - 1] }}
                                        </div>
                                        <select v-else style="font-size: 0.8rem;" class="form-select rounded-0"
                                            aria-label="Default select example" v-model="users[index - 1].role">
                                            <option selected>Роль</option>
                                            <option v-for="j in roles.length" :key="j" :value="roles[j - 1].id">{{
                                                roles[j - 1].name }}</option>
                                        </select>
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Имя</th>
                                    <td>
                                        <div class="text-muted" v-if="edit === false">{{ users[index - 1].first_name }}
                                        </div>
                                        <input v-else v-model="users[index - 1].first_name"
                                            class="form-control form-control-sm" type="text" placeholder=""
                                            aria-label=".form-control-sm example">
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Фамилия</th>
                                    <td>
                                        <div class="text-muted" v-if="edit === false">{{ users[index - 1].last_name }}
                                        </div>
                                        <input v-else v-model="users[index - 1].last_name"
                                            class="form-control form-control-sm" type="text" placeholder=""
                                            aria-label=".form-control-sm example">
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Отчество</th>
                                    <td>
                                        <div class="text-muted" v-if="edit === false">{{ users[index - 1].patronymic }}
                                        </div>
                                        <input v-else v-model="users[index - 1].patronymic"
                                            class="form-control form-control-sm" type="text" placeholder=""
                                            aria-label=".form-control-sm example">
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Статус</th>
                                    <td>
                                        <div class="text-muted" v-if="edit === false">{{ users[index - 1].status }}
                                        </div>
                                        <select v-else v-model="users[index - 1].status"
                                            class="form-select form-select-sm ms-auto text-end"
                                            aria-label=".form-select-sm example">
                                            <option value="Студент">Студент</option>
                                            <option value="Преподаватель">Преподаватель</option>
                                        </select>
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Телефон</th>
                                    <td>
                                        <div v-if="edit === false" class="text-muted">{{ users[index - 1].telephone }}
                                        </div>
                                        <input v-else v-model="users[index - 1].telephone"
                                            class="form-control form-control-sm" type="text" placeholder=""
                                            aria-label=".form-control-sm example">
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" class="align-middle">Активен?</th>
                                    <td>

                                        <label
                                            class="form-check-label  my-auto alert alert-danger text-danger p-1 px-2 rounded-5 text-center  align-middle"
                                            for="flexCheckDefault" v-if="users[index - 1].active === false">
                                            Не активен
                                        </label>

                                        <label
                                            class="form-check-label  my-auto alert alert-success text-success p-1 px-2 rounded-5 text-center  align-middle"
                                            for="flexCheckChecked" v-else>
                                            Активен
                                        </label>

                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="modal-footer">
                        <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                            <button v-if="edit === true" class="btn btn-success"
                                @click="SaveUser(users[index - 1])">Сохранить</button>
                            <button v-if="edit === true" class="btn btn-success" @click="edit = false">Отменить</button>
                            <button v-if="edit === false" type="button" @click="Edit()"
                                class="btn btn-primary">Редактировать</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>-->
        <UserEditModal v-for="index in users.length" @saveUser="SaveUser" :user="users[index - 1]"
            :role="user_roles[index - 1]" :roles="roles_" :ref_index="index"></UserEditModal>
        <ModalDelete @Delete="Delete" @Cancel="Cancel" :object="`User`" :objectType="`пользователя`"
            :objectToDelete="objectToDelete"></ModalDelete>
        <Toast :notificationText="toastString" :color="`green`" :hideToast="hideToast" @hideToast="HideToast()"></Toast>

    </div>
</template>

<script setup>
import axios from "axios";
import Toast from "./Toast.vue"
import userBlock from "../../components/UserBlock.vue";
import { onMounted } from "vue";
import registerError from "../registerComponents/RegisterError.vue";
import ModalDelete from "./../../components/ModalDelete.vue"
import UserEditModal from "./UserEdit.vue";
</script>

<style>
/*
.table-row {
   background-color: rgb(241, 10, 10);
}

.table-row.hover {
   background-color: lightblue !important;
} */

.table-hover tbody tr:hover td,
.table-hover tbody tr:hover th {
    background-color: rgb(239, 252, 255);
}
</style>

<script>
export default {
    props: {
        users_: {
            type: Array,
            required: true,
        },
        roles_: {
            type: Array,
            required: true,
        },
    },
    data(props) {
        //console.log("пользователи 1----")
        let users = props.users_;
        let roles = props.roles_;
        let user_roles = [];
        for (let j = 0; j < users.length; j++) {
            for (let i = 0; i < roles.length; i++) {
                if (roles[i].id === users[j].role) {
                    user_roles.push(roles[i].name);
                    break;
                }
            }
        }

        console.log(props.users_, props.roles_, users, roles)
        return {
            users,
            roles,
            user_roles,
            form: false,
            edit: false,
            hideToast: true,
            toastString: "Пользователь сохранён!",
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
            password: "",
            repeatPassword: "",
            id: "",
            errorId: false,
            isRegister: false,
            errorString: "",
            load: 0,
            objectToDelete: {},

        };
    },
    mounted() {
        console.log("пользователи 2----")

        this.users = this.users_;
        this.roles = this.roles_;

        /*
              //userlist
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
              });
      
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
              }).then((response) => {
                  this.roles = response.data.roles;
              }); */
    },
    watch: {
        users_: {
            handler(newVal, oldVal) {
                this.users = this.users_;
                this.roles = this.roles_;
            },
            deep: true,
        },
    },
    methods: {
        ActivateUser(user) {
            axios({
                method: "put",
                url: this.base_backend_url + "/userlist",
                data: {
                    user: user,
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
                    let new_user = response.data.user;
                    //console.log(response.data)
                    for (let i = 0; i < this.users.length; i++) {
                        if (this.users[i].id === new_user.id) {
                            this.users[i] = new_user;
                            break;
                        }
                    }

                    //this.users = response.data.users;
                    //console.log(response.data);
                });
        },
        OpenUserForm() {
            this.form = !this.form;
        },
        AddUser() {
            this.users.push(this.user);
        },
        DeleteUser(user) {
            console.log(111)
            axios({
                method: "delete",
                url: this.base_backend_url + "/userlist",
                data: {
                    id: user.id,
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
                        this.$emit('deleteUser', response.data.users);
                        console.log(response.data.users);
                    });
                });
        },
        HideToast() {
            this.hideToast = true;
        },
        SaveUser(user) {
            if(user.active === true && user.role===6) {
                user.role=5;
            } 
            if(user.active === false && user.role!==6) {
                user.role=6;
            } 
            axios({
                method: "put",
                url: this.base_backend_url + "/userlist/user_settings",
                data: {
                    user: user,
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
                    console.log(response.data.test)
                    this.hideToast = false;
                    this.edit = false;
                    for (let i = 0; i < this.users.length; i++) {
                        if (this.users[i].id === user.id) {
                            //this.users[i].role === user.role;
                            for (let key in user) {
                                this.users[i][key] = user[key];
                            }
                            for (let j = 0; j < this.roles.length; j++) {
                                if (this.roles[j].id === this.users[i].role) {

                                    this.user_roles[i] = this.roles[j].name;
                                    break;
                                }
                            }
                            this.load++;
                            break;
                        }
                    }
                    //for(let key in user)
                    //for(let i = 0; i <)
                    //let new_user = response.data.user;
                    //console.log(response.data)

                    //this.users = response.data.users;
                    //console.log(response.data);
                });
        },
        /*
        Edit() {
            this.edit = !this.edit;
        }, */
        Register() {
            let canBeAuthorized = true;
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
            console.log("ooo", this.user, canBeAuthorized, "ooo");

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
                    .catch((error) => { })
                    .then((response) => {

                        if (response.data.test === false) {
                            this.errorString = response.data.error;
                            this.errorId = true;
                        } else {
                            this.users.push(response.data.user);
                            this.isRegister = true;
                        }
                    });

                this.isRegister = true;
                this.errorId = false;
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
        ChooseObjectForDelete(object) {
            this.objectToDelete = object;
        },
        Cancel() {
            this.objectToDelete = {};
        },
        Delete(object) {
            this.DeleteUser(object);
        }
    },
};
</script>