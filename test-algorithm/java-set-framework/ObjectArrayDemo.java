class ObjectArrayDemo{
    public static void main(String[] agrs){
        Student[] students = new Student[4];
        
        Student s1 = new Student(20,"fat girl");
        Student s2 = new Student(22,"jason Stark");
        Student s3 = new Student(21,"canada");
        Student s4 = new Student(23,"construction");

        students[0] = s1;
        students[1] = s2;
        students[2] =  s3;
        students[3] =  s4;
    
        for(int i=0;i<students.length;i++)
        {    
            //System.out.println(students[i]);
            System.out.println(students[i].getName()+students[i].getAge());
        }

    }

}
