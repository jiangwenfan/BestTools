public class Student{
    //member variables
    private int age;
    private String name;
    
    //construction method
    public Student(){
        super();

    }
    public Student(int age,String name){
        super();
        this.age = age;
        this.name = name;
    }
    
    public void setAge(int age){
        this.age = age;
    }
    public int  getAge(){
        return age;
    }

    public void setName(String name){
        this.name = name;
    }
    public String getName(){
        return name;
    }
    
    @Override
    public String toString(){
        return "---- name:"+name+"---- age:"+age;
    }
}
