<template>
<div id="app">
  <!-- {{ msg }} -->

  <form @submit.prevent="submitForm">  <!-- "createStudent" -->
    <div class="row m-3">
      <div class="col">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="student.name">
      </div>
      <div class="col">
        <input type="text" class="form-control col-3 mx-2" placeholder="Course" v-model="student.course">
      </div>
      <div class="col">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating" v-model="student.rating">
      </div>
      <div class="col">
        <button class="btn btn-success">Submit</button>
      </div>   
    </div>
  </form>

  <table class="table">
    <thead>
      <th>Name</th>
      <th>Course</th>
      <th>Rating</th>
    </thead>
    <tbody>
      <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
        <td>{{ student.name }}</td>
        <td>{{ student.course }}</td>
        <td>{{ student.rating }}</td>
        <td>
          <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">x</button>
        </td>
      </tr>
    </tbody>
  </table>

</div>
 
</template>

<script>
 

export default {
  name: 'App',
  data(){
    return {
      // msg: 'Hello All'
      student: {},         /// deleted in {...}-> 'name': '', 'course': '','rating': '',
      students: []
    }
  },
  async created(){
    //var response = await fetch('http://127.0.0.1:8000/api/students/')
    //this.students = await response.json();
    await this.getStudents();
  },

  methods: {
    submitForm(){
      if (this.student.id === undefined){
        this.createStudent();
      } else {
        this.editStudent();
      }
    },

    async getStudents(){
      var response = await fetch('http://127.0.0.1:8000/api/students/')
      this.students = await response.json();
    },

    async createStudent(){
      await this.getStudents();
      /*var response = */
      await fetch('http://127.0.0.1:8000/api/students/', {
        method: 'post',
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      //this.students.push(await response.json());
      await this.getStudents();
    },

    async editStudent(){
      await this.getStudents();
      await fetch(`http://127.0.0.1:8000/api/students/${this.student.id}/`, {
        method: 'put', 
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
      this.student = {};
    },

    async deleteStudent(student){
      await this.getStudents();
      await fetch(`http://127.0.0.1:8000/api/students/${student.id}/`, {
        method: 'delete', 
        headers:  {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });
      await this.getStudents();
    },

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

<!-- Link: https://www.youtube.com/watch?v=7GWKv03Osek  -->
