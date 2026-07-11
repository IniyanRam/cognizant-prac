import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCardComponent } from '../course-card/course-card';
import { CourseService } from '../course';

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    CourseCardComponent
  ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css'
})
export class CourseListComponent implements OnInit {

  searchTerm = '';

  loading = false;

  courses: any[] = [];

  constructor(private courseService: CourseService) {}

  ngOnInit(): void {

    this.loading = true;

    this.courseService.getCourses().subscribe((data) => {

      this.courses = data.map((course: any) => ({
        name: course.title,
        code: 'CTS101',
        credits: 4,
        grade: 'A'
      }));

      this.loading = false;

    });

  }

  get filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }

}