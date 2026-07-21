<template>
  <div>
    <h2>Profile</h2>

    <h3>Enrolled Courses</h3>

    <ul>
      <li
        v-for="course in store.enrolledCourses"
        :key="course.id"
      >
        {{ course.name }} ({{ course.credits }} Credits)

        <button @click="store.unenroll(course.id)">
          Remove
        </button>
      </li>
    </ul>

    <h3>Total Credits : {{ store.totalCredits }}</h3>
  </div>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
button {
  margin-left: 10px;
}
</style>