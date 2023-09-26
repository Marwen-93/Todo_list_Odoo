/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component, onWillStart, useState,useRef } = owl;
import { useService } from "@web/core/utils/hooks";





export class Todo extends Component {
    setup() {
        this.state = useState({
            task: { name: '', description: '', color: '#FF0000', is_completed: false },
            taskList: [],
            isedit: false,
            activeId: false
        })
        this.orm = useService('orm');
        this.model = 'todo.list'
        onWillStart(async () => {
            await this.getAllTasks()
        })
        this.inputsearch = useRef("search_Input");
    }
    async getAllTasks() {
        this.state.taskList = await this.orm.searchRead(this.model, [], ['name', 'description', 'color', 'is_completed'])
    }
    addTask(){
        this.resetForm()
        this.state.activeId=false
        this.state.editTask= false


    }
    editTask(task){
        console.log(task)
        this.state.activeId=task.id
        this.state.editTask= true
        this.state.task={...task}
    this.saveTask()

    }
    async saveTask(){
        if (!this.state.activeId){
            await this.orm.create(this.model,[this.state.task])

        } else {
            await this.orm.write(this.model,[this.state.activeId],this.state.task)

        }

        await this.getAllTasks()
    }
    async deleteTask(task){
        console.log('hello ',task)
    await this.orm.unlink(this.model,[task.id])
    await this.getAllTasks()
 }
    resetForm(){
        this.state.task={ name: '', description: '', color: '#FF0000', is_completed: false }
    }
    async searchTask(){
        console.log(this.inputsearch.el.value)
        const text=this.inputsearch.el.value
        this.state.taskList= await this.orm.searchRead(this.model,[['name','ilike',text]],["name","description","color","is_completed"])

    }
    async toggleTask(e,task){
        await this.orm.write(this.model,[task.id],{is_completed:e.target.checked})
        await this.getAllTasks()
    }
    async changeColor(e,task){
        await this.orm.write(this.model,[task.id],{color:e.target.value})
        await this.getAllTasks()
    }

}
Todo.template = "todo_template_js"
registry.category('actions').add('todo.action_todo_list_js', Todo);
