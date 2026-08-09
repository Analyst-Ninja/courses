Notes Link - 
- [Lecture - OOPS](https://docs.google.com/document/d/1uv9EdLaG9TK7iNcMneLeEaChzvmXU9Xu_Uv5iZwswFk/edit?tab=t.0)

### OOPS

4 pillars: Abstraction, Encapsulation, Inheritance, Polymorphism

1. Polymorphism
   - Function Overloading - same name, different params. Resolved at compile time (static binding)
   - Function Overriding - subclass redefines superclass method. Resolved at runtime (dynamic binding)

2. Inheritance

   Arrow points child ---> parent. Solid = `extends`, dotted = `implements`

   Legend: 🟦 parent &nbsp; 🟩 child &nbsp; 🟧 grandchild &nbsp; 🟪 interface

   - Single Level

     ```mermaid
     %%{init: {'theme':'base','themeVariables':{'background':'#ffffff','primaryColor':'#ffffff','primaryTextColor':'#111111','lineColor':'#555555','textColor':'#111111'}}}%%
     graph BT
       Dog --> Animal
       classDef parent fill:#cfe4f7,stroke:#2c6ba0,stroke-width:2px,color:#0d2b45
       classDef child fill:#d6f0dd,stroke:#2f7d4f,stroke-width:2px,color:#123524
       class Animal parent
       class Dog child
     ```

   - Multi Level

     ```mermaid
     %%{init: {'theme':'base','themeVariables':{'background':'#ffffff','primaryColor':'#ffffff','primaryTextColor':'#111111','lineColor':'#555555','textColor':'#111111'}}}%%
     graph BT
       Puppy --> Dog --> Animal
       classDef parent fill:#cfe4f7,stroke:#2c6ba0,stroke-width:2px,color:#0d2b45
       classDef child fill:#d6f0dd,stroke:#2f7d4f,stroke-width:2px,color:#123524
       classDef grand fill:#fbe3cd,stroke:#b3701f,stroke-width:2px,color:#4a2c08
       class Animal parent
       class Dog child
       class Puppy grand
     ```

   - Hierarchical

     ```mermaid
     %%{init: {'theme':'base','themeVariables':{'background':'#ffffff','primaryColor':'#ffffff','primaryTextColor':'#111111','lineColor':'#555555','textColor':'#111111'}}}%%
     graph BT
       Dog --> Animal
       Cat --> Animal
       classDef parent fill:#cfe4f7,stroke:#2c6ba0,stroke-width:2px,color:#0d2b45
       classDef child fill:#d6f0dd,stroke:#2f7d4f,stroke-width:2px,color:#123524
       class Animal parent
       class Dog,Cat child
     ```

   - Hybrid - mix of above, needs an interface in Java

     ```mermaid
     %%{init: {'theme':'base','themeVariables':{'background':'#ffffff','primaryColor':'#ffffff','primaryTextColor':'#111111','lineColor':'#555555','textColor':'#111111'}}}%%
     graph BT
       Dog --> Animal
       Cat --> Animal
       Puppy --> Dog
       Puppy -.-> Pet
       classDef parent fill:#cfe4f7,stroke:#2c6ba0,stroke-width:2px,color:#0d2b45
       classDef child fill:#d6f0dd,stroke:#2f7d4f,stroke-width:2px,color:#123524
       classDef grand fill:#fbe3cd,stroke:#b3701f,stroke-width:2px,color:#4a2c08
       classDef iface fill:#e6d9f5,stroke:#7248a3,stroke-width:2px,color:#2e1a47
       class Animal parent
       class Dog,Cat child
       class Puppy grand
       class Pet iface
     ```

   - Multiple - NOT allowed for classes in Java (diamond problem), do it with interfaces

     ```mermaid
     %%{init: {'theme':'base','themeVariables':{'background':'#ffffff','primaryColor':'#ffffff','primaryTextColor':'#111111','lineColor':'#555555','textColor':'#111111'}}}%%
     graph BT
       Duck -.-> Swimmable
       Duck -.-> Flyable
       classDef child fill:#d6f0dd,stroke:#2f7d4f,stroke-width:2px,color:#123524
       classDef iface fill:#e6d9f5,stroke:#7248a3,stroke-width:2px,color:#2e1a47
       class Swimmable,Flyable iface
       class Duck child
     ```

C++ allows Multiple Inheritance of classes directly. Java forbids it, allows many `implements` instead.

3. Abstraction
   - Show what an object does, hide how it does it or the implementation details
   - Done with `abstract` classes and `interface`
   - An abstract class must be declared with an `abstract` keyword.
   - It can have abstract and non-abstract methods.
   - It cannot be instantiated.
   - It can have constructors and static methods also.
   - It can have final methods which will force the subclass not to change the body of the method.

4. Encapsulation
   - Bundle data + methods in one class, hide state with `private` fields, expose via getters/setters
   - Packages group related classes (organisation), not encapsulation itself

   - 4 Access Modifiers (least to most permissive)
     - private
       - same class only
     - default (package-private, no keyword written)
       - any class in the same package
     - protected
       - same class + same package + subclass in another package (through inheritance only)
     - public
       - any class anywhere
