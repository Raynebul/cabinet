<template>
    <div ref="ProfileEdit" class="modal fade" id="exampleModalEditProfile" tabindex="-1"
        aria-labelledby="exampleModalLabel">
        <div class="modal-dialog">
            <div class="modal-content rounded-0">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">
                        Редактирование профиля
                    </h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
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
                                <th scope="row" class="align-middle">Идентификатор</th>
                                <td class="text-muted">
                                    <div>{{ profile.id }}</div>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Имя пользователя</th>
                                <td class="text-muted">{{ profile.username }}</td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Электронная почта</th>
                                <td class="text-muted">{{ profile.email }}</td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Пароль</th>
                                <td class="text-muted d-flex">
                                    <span class="my-auto">********</span>  
                                    
                                    <a :href="base_frontend_url + `/reset_password`" class="ms-auto btn btn-secondary btn-sm">Сменить пароль</a>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Роль</th>
                                <td>
                                    {{ role.name }}

                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Имя</th>
                                <td>

                                    <input v-model="profile.first_name" class="form-control form-control-sm" type="text"
                                        placeholder="" aria-label=".form-control-sm example">
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Фамилия</th>
                                <td>
                                    <input v-model="profile.last_name" class="form-control form-control-sm" type="text"
                                        placeholder="" aria-label=".form-control-sm example">
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Отчество</th>
                                <td>
                                    <input v-model="profile.patronymic" class="form-control form-control-sm" type="text"
                                        placeholder="" aria-label=".form-control-sm example">
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Статус</th>
                                <td>
                                    <select v-model="profile.status" class="form-select form-select-sm ms-auto text-start"
                                        aria-label=".form-select-sm example">
                                        <option value="Студент">Студент</option>
                                        <option value="Преподаватель">Преподаватель</option>
                                    </select>
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Телефон</th>
                                <td>
                                    <input v-model="profile.telephone" class="form-control form-control-sm" type="text"
                                        placeholder="" aria-label=".form-control-sm example">
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" class="align-middle">Активен?</th>

                                <td>

                                    <label
                                        class="form-check-label  my-auto alert alert-danger text-danger p-1 px-2 rounded-5 text-center  align-middle"
                                        for="flexCheckDefault" v-if="profile.active === false">
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
                    <button class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Отмена</button>
                    <button class="btn btn-primary btn-sm" @click="Save" data-bs-dismiss="modal">Сохранить</button>
                    <!--
                    <div class="btn-group btn-group-sm" role="group" aria-label="Basic example">
                        <button v-if="edit === true" class="btn btn-success"
                            @click="SaveUser(profile)">Сохранить</button>
                        <button v-if="edit === true" class="btn btn-success" @click="edit = false">Отменить</button>
                        <button v-if="edit === false" type="button" @click="Edit()"
                            class="btn btn-primary">Редактировать</button>
                    </div>-->
                    <!--
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Close
              </button>
              <button type="button" class="btn btn-primary">Save changes</button>-->
                </div>
            </div>
        </div>
    </div>
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
            default: () => { },
        },
    },
    data(props) {
        let profile = {};
        for (let key in props.user) {
            profile[key] = props.user[key];
        }
        return {
            profile,
            /*
            changePassword: false,
            newPassword: "",
            validJSON: true,
            errorId: false,
            errorString: "", */
        };
    },
    mounted() {
        this.$refs.ProfileEdit.addEventListener('hidden.bs.modal', event => {
            this.Cancel();
        })
    },
    methods: {
        Save() {
            this.$emit('save', this.profile)
        },
        Cancel() {
            for (let key in this.user) {
                this.profile[key] = this.user[key];
            }
        }
    }
}
</script>