<template>
    <div ref="AddRole" class="modal fade" id="AddRoleModal" tabindex="-1" aria-labelledby="AddRoleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" style="max-width: 66%;">
            <div class="modal-content rounded-0">
                <div class="modal-header">
                    <h5 class="modal-title mx-auto" id="AddRoleModalLabel">Добавление роли</h5>
                    <button type="button" class="btn-close" style="margin: 0; padding: 0" data-bs-dismiss="modal"
                        aria-label="Close" ref="CloseRole"></button>
                </div>
                <div class="modal-body">
                    <table class="table">
                        <thead class="table-success">
                            <tr>
                                <th scope="col" class="align-middle text-center">Название</th>
                                <th scope="col" class="align-middle">Admin</th>
                                <th scope="col" class="align-middle">Trainer</th>
                                <th scope="col" class="align-middle">Course</th>
                                <th scope="col" class="align-middle">Profile</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-size: 0.8rem" class="align-middle text-center text-muted" scope="row">
                                    <input v-model="role.name" class="form-control rounded-0" type="text"
                                        placeholder="Default input" aria-label="default input example">
                                </td>
                                <th style="font-size: 0.8rem" class="align-middle text-center text-muted px-auto"
                                    scope="row">
                                    <div class="form-check">
                                        <input v-model="role.admin" class="form-check-input rounded-5" type="checkbox"
                                            id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">

                                        </label>
                                    </div>
                                </th>
                                <th style="font-size: 0.8rem" class="align-middle text-center text-muted" scope="row">
                                    <div class="form-check">
                                        <input v-model="role.trainer" class="form-check-input  rounded-5"
                                            type="checkbox" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                        </label>
                                    </div>
                                </th>
                                <th style="font-size: 0.8rem" class="align-middle text-center text-muted" scope="row">
                                    <div class="form-check">
                                        <input v-model="role.course" class="form-check-input  rounded-5" type="checkbox"
                                            id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">
                                        </label>
                                    </div>
                                </th>
                                <th style="font-size: 0.8rem" class="align-middle text-center text-muted" scope="row">
                                    <div class="form-check">
                                        <input v-model="role.profile" class="form-check-input  rounded-5"
                                            type="checkbox" id="flexCheckDefault">
                                        <label class="form-check-label" for="flexCheckDefault">

                                        </label>
                                    </div>
                                </th>
                            </tr>
                        </tbody>
                    </table>

                    <!--
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
                                                        <input type="email" v-bind:class="GetEmailClass()"
                                                            id="inputEmail3" v-model="user.email" />
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
                                                    <div v-if="user.password.length === 0" id="textHelp"
                                                        class="form-text">
                                                        От 8 до 20 символов
                                                    </div>
                                                </div>
                                                <div class="mb-3">
                                                    <div class="col-sm-10">
                                                        <label for="inputPasswordAgain3"
                                                            class="col-form-label">Повторите
                                                            пароль<span class="text-danger">*</span></label>
                                                        <input type="password" v-bind:class="GetRepeatPasswordClass()"
                                                            id="inputPasswordAgain3" v-model="repeatPassword"
                                                            aria-describedby="inputGroupPrepend3 validationServerPasswordFeedback"
                                                            required />
                                                        <div v-if="
                                                            repeatPassword != '' &&
                                                            repeatPassword != user.password
                                                        " id="validationServerPasswordFeedback"
                                                            class="invalid-feedback">
                                                            Пароль отличается!
                                                        </div>
                                                        <div v-if="
                                                            repeatPassword != '' &&
                                                            repeatPassword == user.password
                                                        " id="validationServerPasswordFeedback" class="valid-feedback">
                                                            Всё отлично!
                                                        </div>
                                                    </div>
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
                                        
                                        <registerError v-if="errorId === true" />
                                    </div>
                                    <div class="container-fluid text-end">

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>-->
                </div>
                <div class="modal-footer">
                    <button type="submit" class="btn btn-sm btn-primary" @click="AddRole()">
                        Добавить
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from "axios";
</script>

<script>
export default {
    data() {
        return {
            role: {
                name: "Неизвестная роль",
                admin: false,
                profile: false,
                trainer: false,
                course: false,
            },
        };
    },
    mounted() {
        this.$refs.AddRole.addEventListener('hidden.bs.modal', event => {
            //this.Cancel();
            this.role = {
                name: "Неизвестная роль",
                admin: false,
                profile: false,
                trainer: false,
                course: false,
            }
        })
    },
    methods: {
        AddRole() {
            let role = this.role;
            console.log("eelkwe")

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
                    let new_role = response.data.role;
                    this.$emit('AddNewRole', new_role);
                    this.$refs.CloseRole.click();
                });
        },
    },
};
</script>