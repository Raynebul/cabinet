<template>
    <div>
        <div class="d-flex " style="background-color: white;">
            <button disabled @click="AddRole()" class="btn btn-lg rounded-0 btn-success">+</button>
            <h5 class="text-success px-4">
                <div style="padding-top: 10px;">Добавить роль</div>
            </h5>
        </div>
        <table class="table table-striped table-bordered">
            <thead class="table-success">
                <tr>
                    <th scope="col">id</th>
                    <th scope="col">Name</th>
                    <th scope="col">Admin</th>
                    <th scope="col">Trainer</th>
                    <th scope="col">Course</th>
                    <th scope="col">Profile</th>
                    <th scope="col">-</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="i in roles.length" :key="i">
                    <th scope="row">{{ i }}</th>
                    <th scope="row">
                        <div v-if="edit[i - 1] === false">{{ roles[i - 1].name }}</div>
                        <input v-else v-model="roles[i - 1].name" class="form-control rounded-0" type="text"
                            placeholder="Default input" aria-label="default input example">
                    </th>
                    <th scope="row">
                        <div class="form-check">
                            <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-0"
                                type="checkbox" v-model="roles[i - 1].admin" id="flexCheckDefault">
                            <input v-else class="form-check-input rounded-0" type="checkbox"
                                v-model="roles[i - 1].admin" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">

                            </label>
                        </div>
                    </th>
                    <th scope="row">
                        <div class="form-check">
                            <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-0"
                                type="checkbox" v-model="roles[i - 1].trainer" id="flexCheckDefault">
                            <input v-else class="form-check-input rounded-0" type="checkbox"
                                v-model="roles[i - 1].trainer" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                            </label>
                        </div>
                    </th>
                    <th scope="row">
                        <div class="form-check">
                            <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-0"
                                type="checkbox" v-model="roles[i - 1].course" id="flexCheckDefault">
                            <input v-else class="form-check-input rounded-0" type="checkbox"
                                v-model="roles[i - 1].course" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                            </label>
                        </div>
                    </th>
                    <th scope="row">
                        <div class="form-check">
                            <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-0"
                                type="checkbox" v-model="roles[i - 1].profile" id="flexCheckDefault">
                            <input v-else class="form-check-input rounded-0" type="checkbox"
                                v-model="roles[i - 1].profile" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">

                            </label>
                        </div>
                    </th>
                    <th scope="row" style="width: 20rem">
                        <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                            <button v-if="edit[i - 1] === false" @click="Edit(i - 1)" type="button"
                                class="btn btn-primary rounded-0">
                                Редактировать
                            </button>
                            <button v-else @click="Edit(i - 1)" type="button" class="btn btn-warning rounded-0">
                                Отменить
                            </button>
                            <button v-if="edit[i - 1] === true" type="button" class="btn btn-success rounded-0"
                                @click="SaveRole(i - 1)">Сохранить</button>
                        </div>
                    </th>
                </tr>
            </tbody>
        </table>
        <Toast :notificationText="toastString" :color="`green`" :hideToast="hideToast" @hideToast="HideToast()"></Toast>
    </div>

</template>

<script setup>
import axios from "axios";
import Toast from "./userComponents/Toast.vue"
//import roles_ from "../assets/roles.json"
//let roles_ = []
</script>

<script>
export default {
    data() {
        let edit = [];
        let roles_ = []
        let roles = []
        return {
            roles_,
            roles: roles,
            edit,
            hideToast: true,
            toastString: "Роль сохранена!"
        };
    },
    mounted() {
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
            this.roles_ = response.data.roles;
            for (let i = 0; i < this.roles_.length; i++) {
                this.roles.push({});
                for (let object in this.roles_[i]) {
                    this.roles[i][object] = this.roles_[i][object];
                }
            }
            //this.roles = response.data.roles;
            for (let i = 0; i < this.roles_.length; i++) {
                this.edit.push(false);
            }
            console.log(response.data.roles);
        });
    },
    methods: {
        Edit(i) {
            if (this.edit[i] === true) {
                for (let key in this.roles_[i]) {
                    this.roles[i][key] = this.roles_[i][key];
                }
            }
            this.edit[i] = !this.edit[i]
        },
        HideToast() {
            this.hideToast = true;
        },
        SaveRole(i) {
            this.hideToast = false;
            this.edit[i] = false;
        },
        AddRole() {
            let role = {
                name: "Неизвестный пользователь",
                admin: false,
                trainer: false,
                course: false,
                profile: false,

            }
            axios({
                method: "post",
                url: this.base_backend_url + "/rolelist",
                data: {
                    role: role,
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
                    /*
                    if (response.data.test === false) {
                      this.errorString = response.data.error;
                      this.errorId = true;
                    } else {
                      this.isRegister = true;
                    } */
                });
            /*
            this.roles.push({
                name: "swewe",
                profile: false,
                admin: false,
                trainer: false,
                course: false,
            })
            this.roles_.push({
                name: "swewe",
                profile: false,
                admin: false,
                trainer: false,
                course: false,
            })*/
            //this.edit.push(false)
        },
    },
};
</script>

<style></style>