<template>
  <th class="align-middle text-center text-muted" style="font-size: 0.8rem">{{ user.id }}</th>
  <td class="text-muted align-middle" style="font-size: 0.8rem; padding-left: 6%">{{ user.username }}</td>
  <td class="text-muted align-middle" style="font-size: 0.8rem; padding-left: 7%">{{ user.email }}</td>
  <td class="align-middle text-center" style="width: 8em; padding-left: 3%">
    <div class="form-check align-middle" style="font-size: 0.8rem;" v-if="user.active === false">
      <input disabled @click="ActivateUser()" class="form-check-input my-auto rounded-5" style="margin-top: 0.70em !important;"
        type="checkbox" value="" id="flexCheckDefault">
    </div>
    <div class="form-check align-middle" style="font-size: 0.8rem; " v-else>
      <input disabled @click="ActivateUser()" class="form-check-input rounded-5" style="margin-top: 0.70em !important;"
        type="checkbox" value="" id="flexCheckChecked" checked>
    </div>
    <!--
    <div class="form-check align-middle" style="font-size: 0.8rem;" v-if="user.active === false">
      <input @click="ActivateUser()" class="form-check-input my-auto rounded-5" style="margin-top: 0.70em !important;"
        type="checkbox" value="" id="flexCheckDefault">
      <label
        class="form-check-label  my-auto alert alert-danger text-danger p-1 px-2 rounded-5 text-center  align-middle"
        for="flexCheckDefault">
        Не активен
      </label>
    </div>
    <div class="form-check align-middle" style="font-size: 0.8rem; " v-else>
      <input @click="ActivateUser()" class="form-check-input rounded-5" style="margin-top: 0.70em !important;"
        type="checkbox" value="" id="flexCheckChecked" checked>
      <label
        class="form-check-label  my-auto alert alert-success text-success p-1 px-2 rounded-5 text-center  align-middle"
        for="flexCheckChecked">
        Активен
      </label>
    </div>-->
  </td>
  <td class="text-muted align-middle" style="font-size: 0.8rem; padding-left: 5%; width: 18rem;">
    {{ role }}
  </td>
  <!--
  <td class="align-middle text-center">
    <button class="btn btn-success btn-sm rounded-0" @click="SaveUser()">Сохранить</button>
  </td>-->
  <td class="align-middle text-end" style="padding-right: 30px;">
    <button style="
      " type="button" class="profile-icon profile-icon-primary btn btn-outline-primary btn-sm rounded-0 bi bi-gear-fill"
      data-bs-toggle="modal" :data-bs-target="`#exampleModalUser` + user.id">

    </button>
    <button style="
      " class="profile-icon profile-icon-danger btn btn-outline-danger btn-sm bi bi-trash-fill rounded-0" data-bs-toggle="modal"
      data-bs-target="#exampleModalDeleteUser" @click="DeleteUser()"></button>
  </td>
  <!--
    <div
      class="modal fade"
      :id="`exampleModalUser` + user.id"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">
              Информация о пользователе
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Атрибут</th>
                  <th scope="col">Значение</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">id</th>
                  <td>{{ user.id }}</td>
                </tr>
                <tr>
                  <th scope="row">username</th>
                  <td>{{ user.username }}</td>
                </tr>
                <tr>
                  <th scope="row">email</th>
                  <td>{{ user.email }}</td>
                </tr>
                <tr>
                  <th scope="row">password</th>
                  <td>{{ user.password }}</td>
                </tr>
                <tr>
                  <th scope="row">Имя</th>
                  <td>{{ user.first_name }}</td>
                </tr>
                <tr>
                  <th scope="row">Фамилия</th>
                  <td>{{ user.last_name }}</td>
                </tr>
                <tr>
                  <th scope="row">Отчество</th>
                  <td>{{ user.patronymic }}</td>
                </tr>
                <tr>
                  <th scope="row">status</th>
                  <td>{{ user.status }}</td>
                </tr>
                <tr>
                  <th scope="row">Телефон</th>
                  <td>{{ user.telephone }}</td>
                </tr>
                <tr>
                  <th scope="row">Активен?</th>
                  <td>{{ user.active }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  -->
</template>

<script setup>
//import roles from "../assets/roles.json"
</script>

<script>
export default {
  props: {
    user: {
      type: Object,
      required: true,
      default: () => { },
    },
    roles: {
      type: Array,
      default: [],
    }
  },
  data(props) {
    let role = ""
    for (let i = 0; i < props.roles.length; i++) {

      if (props.roles[i].id === props.user.role) {
        role = props.roles[i].name;
        //console.log(props.user, role)
        break;
      }
    }
    return {
      edit: false,
      role: role,
    }
  },
  methods: {
    ActivateUser() {
      this.$emit("activate", this.user);
    },
    DeleteUser() {
      this.$emit("delete", this.user);
    },
    SaveUser() {
      this.$emit("save", this.user);
    },
    Edit() {
      this.edit = !this.edit;
    }
  },
};
</script>