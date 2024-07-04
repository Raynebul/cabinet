<template>
    <div :ref="`EditRole` + String(ref_index)" class="modal fade" :id="`EditRoleModal` + String(ref_index)"
        tabindex="-1" aria-labelledby="EditRoleModalLabel" aria-hidden="true">
        <div class="modal-dialog" style="max-width: 66%;">
            <div class="modal-content rounded-0">
                <div class="modal-header">
                    <h5 class="modal-title mx-auto" id="AddRoleModalLabel">Редактирование роли</h5>
                    <button type="button" class="btn-close" style="margin: 0; padding: 0" data-bs-dismiss="modal"
                        aria-label="Close" :ref="`CloseRoleEdit` + String(ref_index)"></button>
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
                </div>
                <div class="modal-footer">
                    <button data-bs-dismiss="modal" aria-label="Close" type="submit" class="btn btn-sm btn-secondary"
                        >
                        Отмена
                    </button>
                    <button type="submit" class="btn btn-sm btn-primary" @click="SaveRole()">
                        Сохранить
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        role_: {
            Type: Object,
            required: true,
        },
        ref_index: {
            type: Number,
            required: true,
        }
    },
    data(props) {
        let role = {}
        for (let key in props.role_) {
            role[key] = props.role_[key];
        }
        return {
            role,
        }
    },
    mounted() {
        this.$refs["EditRole" + String(this.ref_index)].addEventListener('hidden.bs.modal', event => {
            //this.Cancel();
            for (let key in this.role_) {
                this.role[key] = this.role_[key];
            }
        })
    },
    methods: {
        SaveRole() {
            this.$emit("saveRole", this.role);
            this.$refs[`CloseRoleEdit` + String(this.ref_index)].click();
        }
    }
}
</script>