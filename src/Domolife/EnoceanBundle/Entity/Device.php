<?php

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Device
 *
 * @author clement
 */
namespace Domolife\EnoceanBundle\Entity;
use Doctrine\ORM\Mapping as ORM;
use Gedmo\Mapping\Annotation as Gedmo;
use Doctrine\Common\Collections\ArrayCollection;
use Symfony\Component\Validator\Constraints as Assert;

/**
* @ORM\Entity()
* @ORM\Table(name="device")
*/
class Device {
    /**
    * @ORM\Id
    * @ORM\Column(type="string", length=6, unique=true)
    */
    private $id;
    
    /**
    * @ORM\Column(type="string", length=20)
    */
    private $type;
    

    /**
     * Get id
     *
     * @return integer 
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * Set type
     *
     * @param string $type
     * @return Device
     */
    public function setType($type)
    {
        $this->type = $type;
    
        return $this;
    }

    /**
     * Get type
     *
     * @return string 
     */
    public function getType()
    {
        return $this->type;
    }

    /**
     * Set id
     *
     * @param string $id
     * @return Device
     */
    public function setId($id)
    {
        $this->id = $id;
    
        return $this;
    }
}