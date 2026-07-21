
<template>
  <div>
    <h2>Courses</h2>

    <input
      type="text"
      placeholder="Search course..."
      v-model="searchTerm"
    />

    <div
      v-for="course in filteredCourses"
      :key="course.id"
      class="course"
    >
      <CourseCard
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      />

      <RouterLink :to="'/courses/' + course.id">
        View Details
      </RouterLink>

      <br /><br />

      <button @click="store.enroll(course)">
        Enroll
      </button>

      <hr />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'
import { getAllCourses } from "../api/courseApi";
const store = useEnrollmentStore()

const courses = ref([])
const searchTerm = ref('')

onMounted(async () => {

  try {

    courses.value = await getAllCourses()

  }

  catch (error) {

    console.error(error.message)

  }

})
const filteredCourses = computed(() => {
  return courses.value.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  )
})
</script>

<style scoped>
input {
  padding: 8px;
  margin-bottom: 20px;
  width: 250px;
}

button {
  padding: 8px 15px;
}

.course {
  margin-bottom: 20px;
}
</style>