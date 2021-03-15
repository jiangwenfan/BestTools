class ObjectArrayDemo{
    public static void main(String[] args){
        //create object array 
        Student[] students =  new Student[4];
        
        //create array element
        Student s1 = new Student(22,"fat girl");
        Student s2 = new Student(23,"jason stark");
        Student s3 = new Student(24,"construction ");
        Student s4 = new Student(25,"construction2");

        students[0]=s1;
        students[1] = s2;
        students[2] =  s3;
        students[3] = s4;

        for(int i=0;i<students.length;i++){
System.out.println(students[i]);
}
for(int j =0;j<students.length;j++){
    Student ss = students[j];
    System.out.println("name:----"+ss.getName()+"age:----"+ss.getAge());
}

}

}
