<template>
  <div
    class="modal fade"
    :id="`exampleModalUser` + user_.id"
    :ref="`UserEdit` + ref_index"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5
            class="modal-title"
            id="exampleModalLabel"
            :ref="`UserEditRedact` + ref_index"
            @click=""
          >
            Информация о пользователе
          </h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            :ref="`CloseUserEdit` + ref_index"
            @click="edit = false"
          ></button>
        </div>
        
        <div class="modal-body">
          <table
            class="table table-bordered table-hover"
            style="font-size: 0.8rem"
          >
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
                  <div>{{ user_.id }}</div>
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Username</th>
                <td class="text-muted">{{ user_.username }}</td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Email</th>
                <td class="text-muted">{{ user_.email }}</td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Пароль</th>
                <td class="text-muted">{{ user_.password }}</td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Роль</th>
                <td>
                  <div class="text-muted" v-if="edit === false">{{ role }}</div>
                  <select
                    v-else
                    style="font-size: 0.8rem"
                    class="form-select rounded-0"
                    aria-label="Default select example"
                    v-model="user_.role"
                  >
                    <option selected>Роль</option>
                    <option
                      v-for="j in roles.length"
                      :key="j"
                      :value="roles[j - 1].id"
                    >
                      {{ roles[j - 1].name }}
                    </option>
                  </select>
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Имя</th>
                <td>
                  <div class="text-muted" v-if="edit === false">
                    {{ user_.first_name }}
                  </div>
                  <input
                    v-else
                    v-model="user_.first_name"
                    class="form-control form-control-sm"
                    type="text"
                    placeholder=""
                    aria-label=".form-control-sm example"
                  />
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Фамилия</th>
                <td>
                  <div class="text-muted" v-if="edit === false">
                    {{ user_.last_name }}
                  </div>
                  <input
                    v-else
                    v-model="user_.last_name"
                    class="form-control form-control-sm"
                    type="text"
                    placeholder=""
                    aria-label=".form-control-sm example"
                  />
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Отчество</th>
                <td>
                  <div class="text-muted" v-if="edit === false">
                    {{ user_.patronymic }}
                  </div>
                  <input
                    v-else
                    v-model="user_.patronymic"
                    class="form-control form-control-sm"
                    type="text"
                    placeholder=""
                    aria-label=".form-control-sm example"
                  />
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Статус</th>
                <td>
                  <div class="text-muted" v-if="edit === false">
                    {{ user_.status }}
                  </div>
                  <select
                    v-else
                    v-model="user_.status"
                    class="form-select form-select-sm ms-auto text-start"
                    aria-label=".form-select-sm example"
                  >
                    <option value="Студент">Студент</option>
                    <option value="Преподаватель">Преподаватель</option>
                  </select>
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Телефон</th>
                <td>
                  <div v-if="edit === false" class="text-muted">
                    {{ user_.telephone }}
                  </div>
                  <input
                    v-else
                    v-model="user_.telephone"
                    class="form-control form-control-sm"
                    type="text"
                    placeholder=""
                    aria-label=".form-control-sm example"
                  />
                </td>
              </tr>
              <tr>
                <th scope="row" class="align-middle">Активен?</th>
                <td>
                  <div v-if="edit === false">
                    <div
                      class="form-check align-middle"
                      style="font-size: 0.8rem"
                      v-if="user_.active === false"
                    >
                      <input
                        disabled
                        class="form-check-input my-auto border-secondary"
                        v-model="user_.active"
                        style="margin-top: 0.7em !important"
                        type="checkbox"
                        value=""
                        id="flexCheckDefault"
                      />
                    </div>
                    <div
                      class="form-check align-middle"
                      style="font-size: 0.8rem"
                      v-else
                    >
                      <input
                        disabled
                        class="form-check-input border-secondary"
                        v-model="user_.active"
                        style="margin-top: 0.7em !important"
                        type="checkbox"
                        value=""
                        id="flexCheckChecked"
                        checked
                      />
                    </div>
                  </div>
                  <div v-else>
                    <div
                      class="form-check align-middle"
                      style="font-size: 0.8rem"
                      v-if="user_.active === false"
                    >
                      <input
                        class="form-check-input my-auto border-dark"
                        v-model="user_.active"
                        style="margin-top: 0.7em !important"
                        type="checkbox"
                        value=""
                        id="flexCheckDefault"
                      />
                    </div>
                    <div
                      class="form-check align-middle"
                      style="font-size: 0.8rem"
                      v-else
                    >
                      <input
                        class="form-check-input border-dark"
                        style="margin-top: 0.7em !important"
                        type="checkbox"
                        v-model="user_.active"
                        id="flexCheckChecked"
                        checked
                      />
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div> 
        <div class="modal-footer">
            
          <button
            v-if="edit === true"
            class="btn btn-sm btn-secondary"
            @click="Cancel()"
          >
            Отмена
          </button>
          
          <button
            v-if="edit === true"
            class="btn btn-sm btn-primary"
            @click="SaveUser()"
          >
            Сохранить
          </button>
          
          <button
            v-if="edit === false"
            type="button"
            @click="Edit()"
            class="btn btn-sm btn-primary"
          >
            Редактировать
          </button>
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
    },
    role: {
      type: Object,
      required: true,
    },
    ref_index: {
      type: Number,
      required: true,
    },
    roles: {
      type: Array,
      required: true,
    },
  },
  data(props) {
    //let user_ = props.user;
    let user_ = {};
    for (let key in props.user) {
      user_[key] = props.user[key];
    }
    let role_ = props.role;
    return {
      user_,
      role_,
      edit: false,
    };
  },
  mounted() {
    this.$refs["UserEdit" + String(this.ref_index)].addEventListener(
      "hidden.bs.modal",
      (event) => {
        this.Cancel();
      }
    );
    /*
    this.$refs["UserEdit" + String(this.ref_index)].addEventListener(
      "shown.bs.modal",
      (event) => {
        console.log("что что")
        this.$refs["UserEdit" + String(this.ref_index)].focus();
      }
    ); */
  },
  methods: {
    Edit() {
      //this.edit = !this.edit;
      this.edit = true;
      this.$refs["UserEdit" + String(this.ref_index)].focus();
    },
    SaveUser() {
      this.$emit("saveUser", this.user_);
      this.edit = false;
      this.$refs["UserEdit" + String(this.ref_index)].focus();
    },
    Cancel() {
      this.edit = false;
      for (let key in this.user) {
        this.user_[key] = this.user[key];
      }
      this.$refs["UserEdit" + String(this.ref_index)].focus();
    },
  },
};
</script>
