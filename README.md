# SimulAIverse
This project is a continuation of something I have been wanting to build. It started with a dream to build a simulation 
program in analyzing how various AI models interact with different environments (I know, real original). 
Here are the project specs:

* One crucial requirement is the seamless switching between various models. The ability to transition effortlessly 
between different AI models is key.

* Keep in mind that certain agents may only be compatible with specific types of worlds. However, the world generation
model and the agent model should be adaptable to different terrains and actions, respectively.

* Additionally, it's important for the project to have a user-friendly graphical user interface (GUI) that is visually
appealing. After all, aesthetics do matter!

![simAiverse.jpeg](..%2Fimages%2FsimAiverse.jpg)

## Project Overview
The goal of this project is to develop a simulation program that enables the analysis of how different AI models 
interact with diverse environments. The program aims to provide a seamless switching capability between various models,
allowing researchers and developers to compare and evaluate the performance of different AI algorithms in different 
scenarios.

The simulation program consists of three main components: models, worlds, and agents. The models represent different AI 
algorithms or machine learning models that can be plugged into the simulation. These models may have different 
architectures and learning techniques, enabling a wide range of experimentation possibilities. The worlds component 
focuses on generating different types of terrains or environments for the agents to navigate. The world generation 
models use algorithms or rules to create diverse and realistic scenarios, allowing for testing and 
analysis across various settings.

The agents component encompasses the entities that interact with the environments. Agents can have different 
capabilities and behaviors, and they utilize specific actions to perform tasks within the simulation. The actions 
module provides a variety of predefined actions that agents can choose from, offering flexibility in customizing 
their behavior.

To facilitate usability and enhance the user experience, the simulation program includes a graphical user 
interface (GUI). The GUI provides an intuitive interface for users to interact with the simulation, offering features 
such as model selection, parameter configuration, and real-time visualization of the simulation progress.

The program aims to be user-friendly, visually appealing, and customizable. It allows researchers and developers to 
analyze the performance of different AI models in different environments, gain insights into their strengths and 
weaknesses, and make informed decisions when choosing the most suitable model for specific tasks.
By providing a flexible and modular structure, the simulation program can be extended to incorporate new models, 
actions, and world generation techniques. Documentation will be provided to guide users in understanding and utilizing 
the program effectively, as well as to assist in further development and customization.

## Requirements Analysis
1. Functional Requirements
   * Model Switching: The simulation program should allow for seamless switching between different AI models during 
   runtime, enabling researchers to compare and evaluate their performance.
   * Agent*World Compatibility: The program should support agents that are specifically designed to work with certain 
   types of environments, ensuring compatibility between the agent models and the generated worlds.
   * Action Customization: The simulation program should provide a mechanism for agents to utilize different actions, 
   allowing for customization of their behavior and task performance.
   * Real-time Visualization: The GUI should provide real-time visualization of the simulation, displaying the agent's 
   interactions with the environment and the effects of different models and actions.
2. Non-Functional Requirements
   * User Interface (UI): The GUI should have an intuitive and user-friendly design, making it easy for researchers 
   and developers to navigate and interact with the simulation program.
   * Aesthetics: The GUI should have an appealing visual design, incorporating appropriate colors, fonts, and layout 
   to enhance the user experience.
   * Performance: The simulation program should be able to handle a reasonable number of agents and worlds 
   efficiently, ensuring smooth execution and timely response to user interactions.
   * Extensibility: The program should be designed to be easily extensible, allowing for the addition of new AI 
   models, actions, and world generation techniques without major modifications to the core system.
   * Documentation: Comprehensive documentation should be provided, including user guides, API references, and examples,
   to assist users in understanding and utilizing the simulation program effectively.
3. Additional Considerations
   * Compatibility: The simulation program should be compatible with popular AI frameworks and libraries, facilitating 
   the integration of various AI models into the system.
   * Data Logging: The program may include the capability to log simulation data, such as agent performance metrics, to 
   enable further analysis and offline evaluation.
   * Configuration Management: The program should provide a configuration mechanism to adjust simulation parameters, 
   such as agent speed, world complexity, or model hyperparameters, allowing for fine-tuning and experimentation.

## Architecture Design
The architecture of the simulation program follows a modular and layered approach, allowing for flexibility, 
modifiability, and ease of maintenance. The main components of the architecture are the models, worlds, agents, actions,
GUI, and utility modules.
1. Models
   *   models component represents different AI models or algorithms that can be plugged into the simulation.
   * Each model is implemented as a separate module, following a consistent interface or base class for seamless 
   integration.
   * The models communicate with the rest of the system through standardized methods, enabling easy switching between 
   models and facilitating data exchange.
2. Worlds
	*	The worlds component focuses on generating various terrains or environments for the agents to navigate.
	*	Each world type is implemented as a separate module, encapsulating the logic for generating specific types of 
   worlds.
	*	The world generation modules interact with the agents and models through well-defined interfaces, allowing for 
   compatibility and interaction with different agent capabilities.
3. Agents
	*	The agents component represents the entities that interact with the environments and perform tasks within the 
   simulation.
	*	Each agent model is implemented as a separate module, defining its behavior and capabilities.
	*	The agents can utilize various actions to perform tasks, selecting actions based on their model-specific logic.
	*	The agent models communicate with the world generation modules, actions, and models through standardized 
   interfaces, ensuring compatibility and enabling seamless switching of agents and models.
4. States
	*	The states component includes the implementations of different states that agents and worlds can exhibit.
	*	Each state is implemented as a separate module, defining specific functionality or behavior associated with 
   that state.
	*	Agents can transition between different states based on the changing environment or their internal conditions.
	*	Worlds can also exhibit different states, influencing their behavior or characteristics in the simulation.
	*	The states module provides interfaces or methods that agents, worlds, and models can use to interact with and 
   utilize the specific state functionalities.
5. GUI
	*	The GUI component provides a user-friendly interface for users to interact with the simulation program.
	*	It includes a main window that houses the simulation view, model selection, parameter configuration, and other 
   relevant components.
	*	The GUI interacts with the underlying modules, such as models, worlds, agents, and actions, to display real-time
   visualization and receive user inputs.
	*	The GUI is designed using appropriate frameworks or libraries to achieve a visually appealing and intuitive user
   interface.
6. Utility Modules
	*	Utility modules provide various functionalities and services that are shared across the system.
	*	The model manager module handles the loading, switching, and management of AI models within the simulation.
	*	The world generator module generates different types of terrains or environments for the simulation, based on 
   predefined algorithms or rules.
	*	Other utility modules may include data logging, configuration management, and helper functions to support the 
   overall functionality of the simulation program.
