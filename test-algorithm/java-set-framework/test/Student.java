public class Student{
    //member variable
    private int age;
    private String name;

    //struction method
    public Student(){
        super();
    }
    public Student(int age,String name){
        super();
        this.age = age;
        this.name = name;
    }
        
    //getxx
    public int  getAge(){
        return age;
    }
    public void steAge(int age){
        this.age = age;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    @Override
    public String toString(){
        return "name:"+name+" age:"+age;
    }
}
