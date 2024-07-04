<template>
    <div>
        <!--
        <div class="d-flex " style="background-color: white;">
            <button disabled @click="AddRole()" class="btn btn-lg rounded-0 btn-success">+</button>
            <h5 class="text-success px-4">
                <div style="padding-top: 10px;">Добавить роль</div>
            </h5>
        </div>-->
        <div class="table-responsive" style="width: 100%">
            <table class="table table-hover">
                <thead class="table-success">
                    <tr>
                        <th style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;" scope="col" class="align-middle text-center">#</th>
                        <th scope="col" class="align-middle text-start" style="padding-left: 5%; font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Название</th>
                        <th scope="col" class="align-middle" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Admin</th>
                        <th scope="col" class="align-middle" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Trainer</th>
                        <th scope="col" class="align-middle" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Course</th>
                        <th scope="col" class="align-middle" style="font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Profile</th>
                        <th scope="col" class="align-middle text-end" style="padding-right: 40px; font-size: 0.8rem; font-family: 'Varela Round', sans-serif;">Действие</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="i in roles.length" :key="i">
                        <th style="font-size: 0.8rem" class="align-middle text-center text-muted" scope="row">{{ i }}
                        </th>
                        <td style="font-size: 0.8rem; padding-left: 5%;" class="align-middle text-start text-muted" scope="row">
                            <div v-if="edit[i - 1] === false">{{ roles[i - 1].name }}</div>
                        </td>
                        <th style="font-size: 0.8rem; padding-left: 2%;" class="align-middle text-center text-muted px-auto" scope="row">
                            <div class="form-check">
                                <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-5"
                                    type="checkbox" v-model="roles[i - 1].admin" id="flexCheckDefault">
                            </div>
                        </th>
                        <th style="font-size: 0.8rem; padding-left: 2%;" class="align-middle text-center text-muted" scope="row">
                            <div class="form-check">
                                <input v-if="edit[i - 1] === false" disabled class="form-check-input  rounded-5"
                                    type="checkbox" v-model="roles[i - 1].trainer" id="flexCheckDefault">
                            </div>
                        </th>
                        <th style="font-size: 0.8rem; padding-left: 2%;" class="align-middle text-center text-muted" scope="row">
                            <div class="form-check">
                                <input v-if="edit[i - 1] === false" disabled class="form-check-input  rounded-5"
                                    type="checkbox" v-model="roles[i - 1].course" id="flexCheckDefault">
                            </div>
                        </th>
                        <th style="font-size: 0.8rem; padding-left: 2%;" class="align-middle text-center text-muted" scope="row">
                            <div class="form-check">
                                <input v-if="edit[i - 1] === false" disabled class="form-check-input rounded-5"
                                    type="checkbox" v-model="roles[i - 1].profile" id="flexCheckDefault">
                            </div>
                        </th>
                        <th scope="row" style="width: 20rem; font-size: 0.8rem; padding-right: 30px;"
                            class="align-middle text-end">
                            <!--<div class="btn-group btn-group-sm" role="group" aria-label="Basic example">-->
                            <!--
                        <button v-if="edit[i - 1] === false" @click="Edit(i - 1)" type="button"
                            class="profile-icon btn btn-outline-primary rounded-0 bi bi-pencil-square">

                        </button>-->
                            <button v-if="edit[i - 1] === false" data-bs-toggle="modal"
                                :data-bs-target="`#EditRoleModal` + String(i)" type="button"
                                class="profile-icon profile-icon-primary btn btn-outline-primary btn-sm rounded-0 bi bi-gear-fill">

                            </button>
                            <button v-if="edit[i - 1] === false" data-bs-toggle="modal"
                                data-bs-target="#exampleModalDeleteRole" @click="ChooseObjectForDelete(roles[i - 1])"
                                type="button" class="profile-icon profile-icon-danger btn btn-outline-danger rounded-0 bi bi-trash-fill">

                            </button>
                            <!--
                            <button data-bs-toggle="tooltip" data-bs-placement="top" title="Отмена" v-else
                                @click="Edit(i - 1)" type="button"
                                class="profile-icon btn btn-outline-warning rounded-0 bi bi-backspace-reverse-fill">

                            </button>
                            <button data-bs-toggle="tooltip" data-bs-placement="top" title="Сохранить"
                                v-if="edit[i - 1] === true" type="button"
                                class="profile-icon btn btn-outline-success rounded-0 bi bi-floppy-fill"
                                @click="SaveRole(i - 1)"></button>
                           -->
                        </th>
                    </tr>
                </tbody>
            </table>
        </div>
        <RoleEditModal v-for="index in roles_.length" @saveRole="(new_role) => { SaveRole(new_role, index - 1) }"
            :key="index" :role_="roles_[index - 1]" :ref_index="index"></RoleEditModal>
        <ModalDelete @Delete="Delete" @Cancel="Cancel" :object="`Role`" :objectType="`роль`"
            :objectToDelete="objectToDelete"></ModalDelete>
        <Toast :notificationText="toastString" :color="`green`" :hideToast="hideToast" @hideToast="HideToast()"></Toast>
    </div>

</template>

<script setup>
import axios from "axios";
import Toast from "./Toast.vue"
import ModalDelete from "./../../components/ModalDelete.vue"
import RoleEditModal from "./RoleEdit.vue"
//import roles_ from "../assets/roles.json"
//let roles_ = []
</script>

<script>
export default {
    props: {
        roles_: {
            type: Array,
            required: true,
        },
    },
    data(props) {
        let edit = [];
        //let roles_ = []
        let roles = [];
        for (let i = 0; i < props.roles_.length; i++) {
            roles.push({});
            for (let object in props.roles_[i]) {
                roles[i][object] = props.roles_[i][object];
            }
        }
        for (let i = 0; i < roles.length; i++) {
            edit.push(false);
        }
        return {
            roles: roles,
            edit,
            hideToast: true,
            objectToDelete: {},
            toastString: "Роль сохранена!"
        };
    },
    mounted(props) {
        //rolelist
        this.roles = [];
        for (let i = 0; i < this.roles_.length; i++) {
            this.roles.push({});
            for (let object in this.roles_[i]) {
                this.roles[i][object] = this.roles_[i][object];
            }
        }
        /*
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
        });*/
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
        /*
        SaveRole(i) {
            let saved_role = this.roles[i];
            axios({
                method: "put",
                url: this.base_backend_url + "/rolelist/",
                data: {
                    role: saved_role,
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
                    this.edit[i] = false;
                });

        }, */
        SaveRole(new_role, i) {
            let saved_role = new_role;
            console.log(new_role)

            axios({
                method: "put",
                url: this.base_backend_url + "/rolelist/",
                data: {
                    role: saved_role,
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
                    for (let key in saved_role) {
                        this.roles[i][key] = saved_role[key];
                    }
                    this.$emit('saveRole', saved_role, i);
                    this.edit[i] = false;
                });
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
        DeleteRole(role) {
            console.log(111)
            axios({
                method: "delete",
                url: this.base_backend_url + "/rolelist",
                data: {
                    id: role.id,
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
                    let new_roles = response.data.roles;
                    this.$emit('DeleteRole', new_roles);
                    /*
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
                        console.log(response.data.users);
                    }); */
                });
        },
        ChooseObjectForDelete(object) {
            this.objectToDelete = object;
        },
        Cancel() {
            this.objectToDelete = {};
        },
        Delete(object) {
            this.DeleteRole(object);
        }
    },
};
</script>

<style>
.table-hover tbody tr:hover td,
.table-hover tbody tr:hover th {
    background-color: rgb(239, 252, 255);
}
</style>